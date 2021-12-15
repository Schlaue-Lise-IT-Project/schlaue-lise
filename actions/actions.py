import collections
import logging

from typing import Any, Optional, Text, Dict, List
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.events import SlotSet
from rasa_sdk import FormValidationAction
from rasa_sdk.types import DomainDict

from rasa_sdk import Action, Tracker


logger = logging.getLogger(__name__)
    
class ActionAnswerURL(Action):
    def name(self):
        return "action_answer_url"

    def run(
        self, 
        dispatcher: "CollectingDispatcher", 
        tracker: Tracker, 
        domain: "DomainDict"
    ) -> List[Dict[Text, Any]]:
        url = "Bitte hier klicken, um direkt zur Antwort zu springen:\n"

        slots = tracker.current_slot_values()

        url += f"\nwww.schlaue-lise.de/"

        count = 0
        valueCount = 0

        for slot in slots:
            slotValue = tracker.get_slot(slot)
            if slotValue != None:
                if count > 0:
                    url+= f"&{slot}="
                else: 
                    url += f"?{slot}="
                if isinstance(slotValue, collections.Iterable) & isinstance(slotValue, list):
                    for value in slotValue:
                        if valueCount > 0:
                            url += f"+{value}"
                            valueCount += 1
                        else:
                            url += f"{value}"
                            valueCount += 1
                    valueCount = 0
                else:
                    url += f"{slotValue}"
                count += 1

        dispatcher.utter_message(text=url)

        return []


