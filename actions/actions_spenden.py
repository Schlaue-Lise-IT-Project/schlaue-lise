import collections
import logging
from typing import Any, Optional, Text, Dict, List
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.events import SlotSet
from rasa_sdk import FormValidationAction
from rasa_sdk.types import DomainDict

from rasa_sdk import Action, Tracker

logger = logging.getLogger(__name__)

class ValidateSpendenartikel(FormValidationAction):
    def name(self):
        return "validate_spendenartikel_form"
    
    def validate_spendenartikel(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        if type(slot_value) is list:
            return {"spendenartikel": slot_value}
        else:
            dispatcher.utter_message(text="Es tut mir Leid, aber es scheint nicht geklappt zu haben. Du kannst hier einfach alle gewünschten >>Spendenartikel<< auflisten.")
            return {"spendenartikel": None}

class ValidateSpendeErhalten(FormValidationAction):
    def name(self):
        return "validate_spendeErhalten_form"

    def validate_spendeErhalten(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        if slot_value is not None and type(slot_value) is bool:
            return {"spendeErhalten": slot_value}
        else:
            dispatcher.utter_message(text="Entschuldigung, die Eingabe für >>spendeErhalten<< wurde nicht erkannt. Du kannst auf diese Frage mit 'Ja' oder 'Nein' antworten.")
            return {"spendeErhalten": None}

class ActionAnswerSpende(Action):
    def name(self):
        return "action_answer_spende"

    def run(
        self, 
        dispatcher: "CollectingDispatcher", 
        tracker: Tracker, 
        domain: "DomainDict"
    ) -> List[Dict[Text, Any]]:
        answer = "";

        hygiene_slot = tracker.get_slot("hygieneartikel")
        spendenartikel = tracker.get_slot("spendenartikel")
        spendeErhalten = tracker.get_slot("spendeErhalten")

        spende = list()
        spende_schlafen = list()

        if spendenartikel:
            for item in spendenartikel:
                temp = item.lower()
                if temp == "decke" or temp == "schlafsack" or temp == "isomatte" or temp == "kissen" :
                    spende_schlafen.append(item)
                else:
                    spende.append(item)
        
        if len(spende_schlafen) != 0:
            answer += "Diese Artikel:\n"
            for item in spende_schlafen:
                answer += f"  - {item}\n"
            if spendeErhalten:
                answer += f"\nFindest du bei diesen Stellen: Obdachlosenhilfe"
            else: 
                answer += f"\nKannst du bei diesen Stellen abgeben: Obdachlosenhilfe"

        if len(spende) != 0:
            answer += "\nDiese Artikel:\n"
            for item in spende:
                answer += f"  - {item}\n"
            if spendeErhalten:
                answer += f"\nFindest du bei diesen Stellen: (noch nicht im Prototyp hinterlegt)"
            else: 
                answer += f"\nKannst du bei diesen Stellen abgeben: (noch nicht im Prototyp hinterlegt)"

        if hygiene_slot and len(hygiene_slot) != 0:
            answer += "\nDie Hygieneartikel:\n"
            for item in hygiene_slot:
                answer += f"  - {item}\n"
            if spendeErhalten:
                answer += f"\nFindest du bei diesen Stellen:"
                answer += f"\n - mudra"
                answer += f"\n - Obdachlosenhilfe Nürnberg"
                answer += f"\n - Heinzelmännchen"
                answer += f"\n - Nürnberger Engel"
            else:
                answer += f"\nkönnen nicht gespendet werden."

        dispatcher.utter_message(text=answer)

        return []