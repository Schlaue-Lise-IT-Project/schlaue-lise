import collections
import logging
from typing import Any, Optional, Text, Dict, List
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.events import SlotSet
from rasa_sdk import FormValidationAction
from rasa_sdk.types import DomainDict

from rasa_sdk import Action, Tracker

logger = logging.getLogger(__name__)

class ActionProcessInformAll(Action):
    def name(self) -> Text:
        return "process_inform_all"
    
    def run(
        self, 
        dispatcher: "CollectingDispatcher", 
        tracker: Tracker, 
        domain: "DomainDict"
    ) -> List[Dict[Text, Any]]:
        drug_slot = tracker.get_slot("drogen")
        no_drug_slot = tracker.get_slot("no_drogen")
        pet_slot = tracker.get_slot("haustier")
        no_pet_slot = tracker.get_slot("no_haustier")
        shelter_slot = tracker.get_slot("unterkunft")
        apartment_slot = tracker.get_slot("wohnung")

        petowner = SlotSet("chaustierhalter", None)
        drug_addict = SlotSet("drogenabhaengig", None)
        shelter = SlotSet("unterkunft", None)

        if drug_slot is not None:
            if no_drug_slot is None:
                drug_addict = SlotSet("drogenabhaengig", True)
        else:
            if no_drug_slot is not None:
                drug_addict = SlotSet("drogenabhaengig", False)

        if pet_slot is not None:
            if no_pet_slot is None:
                petowner = SlotSet("chaustierhalter", True)
        else:
            if no_pet_slot is not None:
                petowner = SlotSet("chaustierhalter", False)

        
        if shelter_slot is not None:
            if apartment_slot is None:
                shelter = SlotSet("notunterkunft", True)
        else:
            if apartment_slot is not None:
                shelter = SlotSet("notunterkunft", False)
        
        return [petowner, drug_addict, shelter]

class ValidateInformation(FormValidationAction):
    def name(self) -> Text:
        return "validate_informationen_form"

    def validate_alter(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        try:
            if int(slot_value) >= 18:
                if int(slot_value) >= 22:
                    return {"volljaehrig": True, "jugendlich": False}
                else:
                    return {"volljaehrig": True, "jugendlich": True}
            else:
                return {"volljaehrig": False, "jugendlich": True}
        except:
            dispatcher.utter_message(
                text="Die Eingabe zu >>Alter<< wurde nicht erkannt. Bitte gib eine Zahl an, die dein >>Alter<< darstellt.")
            return {"alter": None}
    
    def validate_bgeschlecht(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        if slot_value.lower() in ["männlich", "weiblich", "divers"]:
            return {"bgeschlecht": slot_value.lower()}
        else:
            dispatcher.utter_message(text="Es tut mir Leid, die Eingabe für dein >>Geschlecht<< wurde nicht erkannt. Bitte gib an, ob du dich als 'männlich', 'weiblich' oder 'divers' bezeichnen würdest.")
            return {"bgeschlecht": None}

    def validate_chaustierhalter(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        if type(slot_value) is bool:
            return {"chaustierhalter": slot_value}
        else:
            dispatcher.utter_message(text="Entschuldigung, die Eingabe zu >>Haustieren<< wurde nicht erkannt. Du kannst auf diese Frage mit 'Ja' oder 'Nein' antworten.")
            return {"chaustierhalter": None}

    def validate_drogenabhaengig(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        if type(slot_value) is bool:
            return {"drogenabhaengig": slot_value}
        else:
            dispatcher.utter_message(
                text="Es tut mir Leid, die Eingabe für >>Drogen<< wurde nicht erkannt. Du kannst auf eine Frage zu >>Drogen<< mit 'Ja' oder 'Nein' antworten.")
            return {"drogenabhaengig": None}

class ValidateNotunterkunft(FormValidationAction):
    def name(self):
        return "validate_unterkunft_form"

    def validate_notunterkunft(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        if slot_value is not None and type(slot_value) is bool:
            return {"notunterkunft": slot_value}
        else:
            dispatcher.utter_message(
                text="Entschuldigung, die Eingabe für >>Notunterkunft<< wurde nicht erkannt. Du kannst auf diese Frage mit 'Ja' oder 'Nein' antworten.")
            return {"notunterkunft": None}