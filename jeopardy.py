# make sure to install module with 'pip install requests'
import requests

# put all code in a function so it won't execute if imported to another file
def main():
    print("Jeopardy!")
    # call the jservice API and get a random question
    response = requests.get("http://jservice.io/api/random")
    # make sure the HTTP Response is "200 OK"
    if response.status_code != 200:
        # display an error message with the response code and reason
        print(f"Couldn't get question from jservice.io: {response.status_code}: {response.reason}")
        # quit with a non-zero return code to indicate an error
        exit(1)
    else:
        # convert the response to a JSON object
        # the JSON is an array so get the first and only item
        question = response.json()[0]

        print(f"Question ID: {question['id']}")
        print(f"Category: {question['category']['title']} (id: {question['category']['id']})")
        print(f"Value: {question['value']}")
        print(f"Question: {question['question']}")
        print(f"Answer: {question['answer']}")
        print(f"Airdate: {question['airdate']}")

# check to see if running as a script and execute the main function
# this will keep it from running if imported from another script
if __name__ == '__main__':
    main()