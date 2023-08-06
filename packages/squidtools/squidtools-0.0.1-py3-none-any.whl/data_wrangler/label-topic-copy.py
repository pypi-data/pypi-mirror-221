import openai
from openai import error
import os
import time
import argparse
import json
import sys

openai.api_key = os.environ["OPENAI_KEY"]

MAX_ATTEMPTS = 5
SKIP_EXISTING = True

IDENTIFY_PROMPT = """
Does the following news article excerpt contain discussion of
the science of climate change, global warming, or impacts of climate change or climate change related policy? 
Be concise. End your answer with either "yes" or "no".
"""


# utility functions for handling open AI responses
def basic_prompt(prompt, input, big_context=False):
    messages = [{"role": "user", "content": f"{prompt}\n{input}"}]
    response = generate_chat_response(messages, big_context)
    return get_message_text(response), get_total_cost(response)


def generate_chat_response(messages, big_context=False, attempt=0):
    if big_context:
        model = "gpt-3.5-turbo-16k"
    else:
        model = "gpt-3.5-turbo"
    try:
        response = openai.ChatCompletion.create(
            model=model,
            temperature=0.5,
            messages=messages,
        )
        return response
    except error.ServiceUnavailableError as e:
        attempt += 1
        if attempt > MAX_ATTEMPTS:
            raise e

        sleeptime = pow(2, attempt + 1)
        sys.stderr.write("Service Unavailable.. sleeping for " + str(sleeptime) + "\n")
        sys.stderr.flush()
        time.sleep(sleeptime)
        return generate_chat_response(messages, big_context, attempt)
    except error.APIError as e:
        if "bad gateway" in str(e).lower():
            # bad gateway, we retry
            attempt += 1
            if attempt > MAX_ATTEMPTS:
                raise e
            sleeptime = pow(2, attempt + 1)
            print(f"Bad Gateway. Sleeping for {sleeptime}s.")
            time.sleep(sleeptime)
            return generate_chat_response(messages, big_context, attempt)
        else:
            raise e


def get_message_text(response):
    return response.choices[0].message.content


def get_total_tokens(responses):
    return sum([r.usage.total_tokens for r in responses])


def get_total_cost(responses):
    input_costs = {
        "gpt-3.5-turbo-0613": 0.0015 / 1000,
        "gpt-3.5-turbo-16k-0613": 0.003 / 1000,
    }
    output_costs = {
        "gpt-3.5-turbo-0613": 0.002 / 1000,
        "gpt-3.5-turbo-16k-0613": 0.004 / 1000,
    }
    # check if models are present
    for r in responses:
        if r["model"] not in input_costs:
            sys.stderr.write(f"{r['model']} not found in input costs! update please")
            return -1

    return sum(
        [
            r.usage.prompt_tokens * input_costs[r["model"]]
            + r.usage.completion_tokens * output_costs[r["model"]]
            for r in responses
        ]
    )

def label_lines(lines):
    response = basic_prompt(IDENTIFY_PROMPT, "\n".join(lines))
    cost = get_total_cost([response])
    message = get_message_text(response)
    label = None
    if 'yes' in message.lower() and 'no' not in message.lower():
        label = True
    elif 'no' in message.lower():
        label = False
    else:
        print("Both no and yes in the response?")
    return label, cost


def make_paragraphs(f):
    text = "\n".join([lines.strip() for lines in f])
    return text.split("\n\n")


def label_file(filename):
    with open(filename, "rt") as f:
        lines = make_paragraphs(f)
        label, cost = label_lines(lines[0:5])
        results = {"filename": filename, "label": label, "cost": cost}
        return results

# Progress capture is implemented as lines of json in a file
# This way we can append easily to the file without thrashing the disk
PROGRESS_FILENAME = 'progress.json'
def load_progress():
    progress = {}
    if os.path.exists(PROGRESS_FILENAME):
        with open(PROGRESS_FILENAME, 'rt') as f:
            for line in f:
                p = json.loads(line)
                progress[p.filename] = p
    return progress


# Save the result to disk
def save_progress(filename, result):
    with open(PROGRESS_FILENAME, 'at') as f:
        f.write(json.dumps(result) + '\n')


def label_dir_robust(dirname, skip_existing=True):
    progress = load_progress()
    for filename in os.listdir(dirname):
        if filename.endswith(".txt"):
            if skip_existing and filename in progress:
                continue
            file_path = os.path.join(dirname, filename)
            results = label_file(file_path) 
            save_progress(filename, results)
            progress[filename] = results
    return progress


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Use ChatGPT to label news articles."
    )
    parser.add_argument(
        "path",
        type=str,
        help="Path to the txt file(s). If directory, extracts for every .txt file in the directory",
    )

    args = parser.parse_args()
    if os.path.isdir(args.path):
        results = label_dir_robust(args.path)
        print(json.dumps(results, indent=4))
    else:
        res = label_file(args.path)
        print(json.dumps(res, indent=4))
