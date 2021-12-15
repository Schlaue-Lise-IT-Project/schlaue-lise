import collections
import logging
from typing import Any, Optional, Text, Dict, List
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.events import SlotSet
from rasa_sdk import FormValidationAction
from rasa_sdk.types import DomainDict

from rasa_sdk import Action, Tracker

logger = logging.getLogger(__name__)

class ValidateMedicineForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_medicine_form"

    def validate_emergency(
        self,
        slot_value: bool,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:

        # zeigt beim nächsten mal slot_value-type an
        text = f">>>>Slot emergency ist gesetzt auf '{slot_value}' und vom Typ {type(slot_value)}"

        intent = tracker.latest_message['intent'].get('name')

        if(intent == 'affirm'):
            return{"emergency": True}
        elif(intent == 'deny'):
            return{"emergency": False}
        elif(intent == 'medicine_specific_emergency' or intent == 'medicine_all_information'):
            return {"emergency": slot_value}
        else:
            dispatcher.utter_message(
                text="Entschuldigung, die Eingabe zu >>Notfall<< wurde nicht erkannt. Du kannst auf diese Frage mit 'Ja' oder 'Nein' antworten.")
            return {"emergency": None}

    def validate_insurancestatus(
            self,
            slot_value: bool,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,) -> Dict[Text, Any]:

        intent = tracker.latest_message['intent'].get('name')

        if(intent == 'affirm'):
            return{"insurancestatus": True}
        elif(intent == 'deny'):
            return{"insurancestatus": False}
        elif(intent == 'medicine_specific_insurancestatus' or intent == 'medicine_all_information'):
            return {"insurancestatus": slot_value}
        else:
            dispatcher.utter_message(
                text="Entschuldigung, die Eingabe zu >>Versicherungsstatus<< wurde nicht erkannt. Du kannst auf diese Frage mit 'Ja' oder 'Nein' antworten.")
            return {"insurancestatus": None}