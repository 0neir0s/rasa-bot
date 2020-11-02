# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher

class ActionJoke(Action):

    def name(self) -> Text:
        return "action_joke"

    def getJoke(self, joke_type: bool) -> str:
        Jokes = { 
            True: "What was going through the minds of all of Chuck Norris' victims before they died? His shoe.",
            False: "MacGyver can build an airplane out of gum and paper clips. Chuck Norris can kill him and take it."
        } 
        return Jokes[joke_type]

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        joke_type = tracker.get_slot("joke_type") == 'good'
        dispatcher.utter_message(text= self.getJoke(joke_type))
        return [AllSlotsReset()]

class ActionTCM(Action):

    def name(self) -> Text:
        return "action_tcm"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        currency, order_side = tracker.get_slot("currency"), tracker.get_slot("order_side")
        order_type, quantity = tracker.get_slot("order_type"), tracker.get_slot("quantity")
        dispatcher.utter_message(text=f'TCM for the Algo {order_type} order of {quantity}-{currency} {order_side} is 1.34')
        return [AllSlotsReset()]