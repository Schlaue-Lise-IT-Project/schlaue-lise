import collections
import logging
from typing import Any, Optional, Text, Dict, List
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.events import SlotSet
from rasa_sdk import FormValidationAction
from rasa_sdk.types import DomainDict

from rasa_sdk import Action, Tracker

logger = logging.getLogger(__name__)

class ValidateHygieneartikel(FormValidationAction):
    def name(self):
        return "validate_hygiene_form"
    
    def validate_hygieneartikel(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        if type(slot_value) is list:
            return {"hygieneartikel": slot_value}
        else:
            dispatcher.utter_message(
                text="Es tut mir Leid, aber es scheint nicht geklappt zu haben. Du kannst hier einfach alle gewünschten >>Hygieneartikel<< auflisten.")
            return {"hygieneartikel": None}

class ActionAnswerHygiene(Action):
    def name(self):
        return "action_answer_hygiene"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict"
    ) -> List[Dict[Text, Any]]:
        answer = "Alles klar. Diese Artikel:\n"

        slot_value = tracker.get_slot("hygieneartikel")

        for item in slot_value:
            answer += f"  - {item}\n"

        answer += f"\nFindest du bei diesen Stellen:"
        answer += f"\n - mudra"
        answer += f"\n - Obdachlosenhilfe Nürnberg"
        answer += f"\n - Heinzelmännchen"
        answer += f"\n - Nürnberger Engel"

        dispatcher.utter_message(text=answer)

        return []

