# This files contains your custom actions which can be used to run
# custom Python code.

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


        
class ActionTranslateCertificates(Action):
    def name(self) -> str:
        return "action_translate_certificates"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:

        certificate_type = tracker.get_slot('certificate_type')
        
        if certificate_type == 'general certificate':
            dispatcher.utter_message(response="utter_general_certificate")
        elif certificate_type == 'language certificate':
            dispatcher.utter_message(response="utter_language_certificate")
        elif certificate_type == 'subject certificate':
            dispatcher.utter_message(response="utter_subject_certificate")
        else:
            dispatcher.utter_message(response="utter_certificate_default")

        return []
    
class ActionProvideLanguageQualificationsInfo(Action):
    def name(self) -> str:
        return "action_provide_language_qualifications_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:

        department = tracker.get_slot('department')

        if department == 'informatics':
            dispatcher.utter_message(response="utter_informatics_language_requirements")
        elif department == 'applied science':
            dispatcher.utter_message(response="utter_applied_science_language_requirements")
        elif department == 'physics':
            dispatcher.utter_message(response="utter_physics_language_requirements")
        else:
            dispatcher.utter_message(response="utter_general_language_requirements")

        return []

class ActionHandleSubjectEqualizing(Action):
    def name(self) -> str:
        return "action_handle_subject_equalizing"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        last_intent = tracker.latest_message['intent'].get('name')

        if last_intent == 'inform_subject_completion':
            dispatcher.utter_message(response="utter_already_did_subject")
        elif last_intent == 'inform_having_certificate':
            dispatcher.utter_message(response="utter_have_corresponding_certificate")
        elif last_intent == 'inform_qualification':
            dispatcher.utter_message(response="utter_have_appropriate_qualification")
        else:
            dispatcher.utter_message(response="utter_ask_subject_equalizing")

        return []
    
class ActionExtraSubjectsInfo(Action):
    def name(self) -> str:
        return "action_extra_subjects_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        semester_number = tracker.get_slot('semester_number')

        if semester_number == 'first':
            dispatcher.utter_message(response="utter_semester_1_options")
        elif semester_number == 'third' or semester_number == 'fifth':
            dispatcher.utter_message(response="utter_semester_3_and_5_options")
        else:
            dispatcher.utter_message(response="utter_general_info_on_extra_subjects")
        
        return []
    
class ActionFinancialAidInfo(Action):
    def name(self) -> str:
        return "action_financial_aid_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        residence_status = tracker.get_slot('residence_status')

        if residence_status == 'EU citizen':
            dispatcher.utter_message(response="utter_eu_citizen")
        elif residence_status == "resident":
            dispatcher.utter_message(response="utter_resident")
        elif residence_status == "refugee":
            dispatcher.utter_message(response="utter_refugee")
        elif residence_status == "immigrant":
            dispatcher.utter_message(response="utter_immigrant")
        else:
            dispatcher.utter_message(response="utter_residence_status")

        return []