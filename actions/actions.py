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
        return "action_check_vacant_beds"

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

        dispatcher.utter_message(text=top_five)
        dispatcher.utter_message(response="utter_also_check")
        # video='https://youtu.be/VdTviH5Svzc'
        # image1="https://img.youtube.com/vi/{}/maxresdefault.jpg".format(video.split('/')[-1])
        # dispatcher.utter_message(response="Watch this video: \n"+video,image=image1)
        dispatcher.utter_message(text="<h2>Is there anything else that i can help you with?<h2>",buttons=[
            {"title":"Yes","payload":"/affirm"},
            {"title":"NO","payload":"/deny"},
        ])

        return []


class ActionCheckNonVacantBeds(Action):

    def name(self) -> Text:
        return "action_check_non_icu_vacant_beds"

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
        # video = 'https://youtu.be/VdTviH5Svzc'
        # image1 = "https://img.youtube.com/vi/{}/maxresdefault.jpg".format(video.split('/')[-1])
        # dispatcher.utter_message(response="Watch this video:\n " + video, image=image1)
        dispatcher.utter_message(text="Is there anything else that i can help you with?", buttons=[
            {"title": "Yes", "payload": "/affirm"},
            {"title": "NO", "payload": "/deny"},
        ])
        return []



class ActionResourcesList(Action):

    def name(self) -> Text:
        return "action_resources_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        test_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [{
                    "title": "Innovate Youself",
                    "subtitle": "Get It, Make it.",
                    "image_url": "static/test.jpg",
                    "buttons": [{
                        "title": "Innovate Yourself",
                        "url": "https://www.innovationyourself.com/",
                        # "https://yt3.ggpht.com/ytc/AAUvwnhZwcqP89SH71KugPDfltbcpBajoPpxihN7aPGOmzE=s900-c-k-c0x00ffffff-no-rj",
                        "type": "web_url"
                    },
                        {
                            "title": "Innovate Yourself",
                            "type": "postback",
                            "payload": "/greet"
                        }
                    ]
                },
                    {
                        "title": "RASA CHATBOT",
                        "subtitle": "Conversational AI",
                        "image_url": "static/rasa.png",
                        "buttons": [{
                            "title": "Rasa",
                            "url": "https://www.rasa.com",
                            "type": "web_url"
                        },
                            {
                                "title": "Rasa Chatbot",
                                "type": "postback",
                                "payload": "/greet"
                            }
                        ]
                    }
                ]
            }
        }
        covid_resources = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [{
                    "title": "MBMC",
                    "subtitle": "FIND BED, SAVE LIFE.",
                    "image_url": "static/hospital-beds-application.jpg",
                    "buttons": [{
                        "title": "Hospital Beds Availability",
                        "url": "https://www.covidbedmbmc.in/",
                        "type": "web_url"
                    },
                        {
                            "title": "MBMC",
                            "type": "postback",
                            "payload": "/affirm"
                        }
                    ]
                },
                    {
                        "title": "COVID.ARMY",
                        "subtitle": "OUR NATION, SAVE NATION.",
                        "image_url": "static/oxygen-cylinder-55-cft-500x554-500x500.jpg",
                        "buttons": [{
                            "title": "COVID ARMY",
                            "url": "https://covid.army/",
                            "type": "web_url"
                        },
                            {
                                "title": "COVID ARMY",
                                "type": "postback",
                                "payload": "/deny"
                            }
                        ]
                    },
                    {
                        "title": "Innovate Youself",
                        "subtitle": "Get It, Make it.",
                        "image_url": "static/test.jpg",
                        "buttons": [{
                            "title": "Innovate Yourself",
                            "url": "https://www.innovationyourself.com/",
                            # "https://yt3.ggpht.com/ytc/AAUvwnhZwcqP89SH71KugPDfltbcpBajoPpxihN7aPGOmzE=s900-c-k-c0x00ffffff-no-rj",
                            "type": "web_url"
                        },
                            {
                                "title": "Innovate Yourself",
                                "type": "postback",
                                "payload": "/greet"
                            }
                        ]
                    },
                    {
                        "title": "RASA CHATBOT",
                        "subtitle": "Conversational AI",
                        "image_url": "static/rasa.png",
                        "buttons": [{
                            "title": "Rasa",
                            "url": "https://www.rasa.com",
                            "type": "web_url"
                        },
                            {
                                "title": "Rasa Chatbot",
                                "type": "postback",
                                "payload": "/greet"
                            }
                        ]
                    }
                ]
            }
        }

        dispatcher.utter_message(attachment=covid_resources)
        return []
