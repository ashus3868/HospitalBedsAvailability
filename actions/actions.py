# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import time
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from main import bed_availability


class ActionCheckVacantBeds(Action):

    def name(self) -> Text:
        return "action_check_non_icu_vacant_beds"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # time.sleep(2)
        beds = "https://www.covidbedmbmc.in/HospitalInfo/show"
        extract_output=bed_availability(beds)
        sorted_result=sorted(extract_output,key=lambda x:x[4],reverse=True)
        dispatcher.utter_message(text="Here are the top 5 hospitals having maximum vacant beds with there contact details,")
        top_five=""
        for (hospital_name, contact, vacant, icu_vacant, non_icu_vacant) in sorted_result[:5]:
            # if contact is not None:
                top_five+='''Hospital: {} ,
Contact: {} ,
Total Vacant: {} ,
Non ICU Vacant: {} ,
Location: "[{}](https://www.google.co.in/maps/search/{})"  ,
{}\n'''.format(hospital_name, contact, vacant, non_icu_vacant, hospital_name, hospital_name.strip().replace(" ", "+"), "*" * 50)

        # print(top_five)
        dispatcher.utter_message(text=top_five)
        dispatcher.utter_message(response="utter_also_check")
        dispatcher.utter_message(text="Is there anything else that i can help you with?",buttons=[
            {"title":"Yes","payload":"/affirm"},
            {"title":"NO","payload":"/deny"},
        ])
        return []


class ActionCheckVacentBeds(Action):

    def name(self) -> Text:
        return "action_check_icu_vacant_beds"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # time.sleep(2)
        beds = "https://www.covidbedmbmc.in/HospitalInfo/show"
        extract_output=bed_availability(beds)
        sorted_result=sorted(extract_output,key=lambda x:x[3],reverse=True)
        dispatcher.utter_message(text="Here are the top 5 hospitals having maximum vacant beds with there contact details,")
        top_five=""
        for (hospital_name, contact, vacant, icu_vacant, non_icu_vacant) in sorted_result[:5]:
            # if contact is not None:
                top_five+='''Hospital: {} ,
Contact: {} ,
Total Vacant: {} ,
ICU Vacant: {} ,
Location: "[{}](https://www.google.co.in/maps/search/{})"  ,
{}\n'''.format(hospital_name, contact, vacant, icu_vacant,hospital_name,hospital_name.strip().replace(" ","+"), "*" * 50)

        # print(top_five)
        dispatcher.utter_message(text=top_five)
        dispatcher.utter_message(response="utter_also_check")
        dispatcher.utter_message(text="Is there anything else that i can help you with?", buttons=[
            {"title": "Yes", "payload": "/affirm"},
            {"title": "NO", "payload": "/deny"},
        ])
        return []
