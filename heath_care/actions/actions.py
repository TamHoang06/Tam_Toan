from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionUtterPresent(Action):
    def name(self) -> Text:
        return "utter_present"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hi! I am your chatbot. How can I assist you today?")
        return []

class ActionUtterGreetings(Action):
    def name(self) -> Text:
        return "utter_greetings"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello! How can I help you?")
        return []

class ActionUtterGoodbye(Action):
    def name(self) -> Text:
        return "utter_goodbye"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Goodbye! Have a great day!")
        return []

class ActionUtterAgree(Action):
    def name(self) -> Text:
        return "utter_agree"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Great! Glad we agree.")
        return []

class ActionUtterDisagree(Action):
    def name(self) -> Text:
        return "utter_disagree"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="I understand. Let's discuss further.")
        return []

class ActionUtterJoke(Action):
    def name(self) -> Text:
        return "utter_joke"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Why don't scientists trust atoms? Because they make up everything!")
        return []

# Health-related actions
class ActionUtterCommonColdSymptoms(Action):
    def name(self) -> Text:
        return "utter_common_cold_symptoms"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Common cold symptoms include a runny nose, sore throat, coughing, and sneezing.")
        return []

class ActionUtterCommonColdDefine(Action):
    def name(self) -> Text:
        return "utter_common_cold_define"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="A common cold is an upper respiratory tract infection caused by a virus.")
        return []

class ActionUtterCommonColdPrevention(Action):
    def name(self) -> Text:
        return "utter_common_cold_prevention"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="To prevent a common cold, wash your hands regularly and avoid close contact with sick individuals.")
        return []

class ActionUtterEndAdvice(Action):
    def name(self) -> Text:
        return "utter_end_advice"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="If you have any other questions, feel free to ask!")
        return []

# Similar actions for other health topics would be implemented here following the same pattern

