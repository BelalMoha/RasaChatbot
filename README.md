Belal Mohamed

# University Integration Assisstant

Git Repository: https://mygit.th-deg.de/bm13068/chatbot

wiki: https://mygit.th-deg.de/bm13068/chatbot/-/wikis/home

## Project Description
The Chatbot aims to help immigrant students in their university studies and integration, aiding with course applications, different subjects, and more.

The System Persona,Lina Fritz, Provides specific help according to requests

## Installation

### Prerequisites

- **Python Version**: Ensure Python 3.9.13 (64-bit) or newer is installed on your system.
- **Rasa Version**: Rasa 3.6.15 (Minimum Compatible Version: 3.5.0).
- **Rasa SDK Version**: 3.6.2.
- **Werkzeug Version**: Werkzeug 3.0.1.

### Installation Steps

1. **Clone the Repository**:https://mygit.th-deg.de/bm13068/chatbot
cd chatbot

2. **Run Rasa Actions**:
In a new terminal, execute:rasa run actions

3. **Start Rasa Shell**:
After training, begin the Rasa interactive chat interface:rasa shell

## Basic Usage

### Starting the Project
To start using the University Integration Assisstant:

**Launch the Rasa Chatbot**: 
   - Open a new terminal.
   - Execute `rasa run actions` to start the Rasa actions server.
   - In another terminal, train the Rasa model using `rasa train`.
   - Once the training is complete, start the Rasa shell with `rasa shell` to interact with the chatbot.


### Key Use Cases
- **Translating Certificates**: Users can ask about how to translate different types of certificates through the university
- **Language Qualifications**: Users can inquire about different language requirements for different departments
- **Subject Equalising**: Users can ask to equalise subjects or certificates through the university
- **Extra Subjects**: Users can ask about extra subjects they can take depending on their semester
- **Financial Aid**: Users can get info about requirements for financial aid at the university

## Implementations of the Requests

In the nlu.yml inside the data folder, the use cases are implemented
In the domain.yml, the intents and slots are implemented
In the endpoints.yml, the server host is found
In the actions folder, the __init__.py is the initialisation of the bot, and actions.py are the custom actions for our project
- **Action Classes**: Each action class in `actions.py` corresponds to a specific user query that the chatbot can handle. For example:
  - `ActionTranslateCertificates` interacts with the Flask server to display information about certificate translation through the university.
  - `ActionProvideLanguageQualificationsInfo` retrieves information about language qualifications.
  - Other actions (`ActionHandleSubjectEqualizing`, `ActionExtraSubjectsInfo`, etc.) similarly fetch and provide specific information in response to user queries.


## Work Done

Use Cases, Dialogue Flow, Personas, Dialogue Examples, Domain(first version), Domain(final version), yml implementation

Custom actions

## Missing Parts

The project had a 6th use case. It was removed towards the end because of problems during implementation. 

Currently, the first Custom action, `ActionTranslateCertificates`, currently jumps directly to the 'else' clause in our action, so it doesn't work. 
