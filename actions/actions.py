
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
        text = f">>>>Slot emergency ist gesetzt auf '{slot_value}' und vom Typ {logger.info(type(slot_value))}"

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

    def validate_geschlecht(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        if slot_value.lower() in ["männlich", "weiblich", "divers"]:
            return {"geschlecht": slot_value}
        else:
            dispatcher.utter_message(
                text="Es tut mir Leid, die Eingabe für dein >>Geschlecht<< wurde nicht erkannt. Bitte gib an, ob du dich als 'männlich', 'weiblich' oder 'divers' bezeichnen würdest.")
            return {"geschlecht": None}

    def validate_haustierhalter(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        if type(slot_value) is bool:
            return {"haustierhalter": slot_value}
        else:
            dispatcher.utter_message(
                text="Entschuldigung, die Eingabe zu >>Haustieren<< wurde nicht erkannt. Du kannst auf diese Frage mit 'Ja' oder 'Nein' antworten.")
            return {"haustierhalter": None}

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


class ValidateHygieneartikel(FormValidationAction):
    def name(self):
        return "validate_hygieneliste_form"

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

        dispatcher.utter_message(text=answer)

        return []
