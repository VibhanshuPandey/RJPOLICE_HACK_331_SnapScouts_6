from flask import Flask,jsonify

class User:

    def signup(self):

        user = {
            "_id":"",
            "username":"",
            "password":"",
            "email":"",
            "mobile_no":""          
        }
        return jsonify(user), 200

class Camera:

    def cam_reg(self):

        camera = {
            "_id":"",
            "camera_name":"",
            "camera_type":"",
            "camera_model":"",
            "camera specs":"",
            "location_coordinates":"",
            "address":"",
            "visibility_range_description":"",
            "access_code":"",
            "2FA":""  
        }
        return jsonify(camera), 200

class TermsAndConditions:
    def tandc(self):

        termsandcond = {
            "_id":"",
            "user_agreement":"",
            "consent_to_share_data":""
        } 
        return jsonify(termsandcond), 200
    
class EmergencyContact:

    def emergencycontact(self):
        e_contact = {
            "_id":"",
            "emergency_contact":"",
            "emergency_contact_phone_number":""
        }
        return jsonify(e_contact), 200


class NotificationPreferences:

    def notificationpreferences(self):
        noti_pref= {
            "_id":"",
            "communication_preferences":"",
            "alert_settings":""
        }
        return jsonify(noti_pref), 200

class LicenseAgreement:

    def licenseagreement(self):
        license = {
            "_id":"",
            "camera_licensing_information":""
        }
        return jsonify(license), 200