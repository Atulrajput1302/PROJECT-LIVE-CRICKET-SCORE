import requests
from datetime import datetime
from twilio.rest import Client
#---------------------------------------------------------------------------------------------------------------------------------------------------------

class ScoreGet:

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        self.url_get_all_matches = "http://cricapi.com/api/matches"             #gets all the matches
        self.url_get_score="http://cricapi.com/api/cricketScore"                #gets the score for a unique_id
        self.api_key = "burAILHnUxRSkXR84XTETR0UWdH2"                           #Unique for every user
        self.unique_id = ""

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    def get_unique_id(self):
        uri_params = {"apikey" : self.api_key}
        response = requests.get(self.url_get_all_matches, params= uri_params)
        response_json = response.json()      #converting to JSON format: becomes easy to extract data
        data = response_json['matches']      #accesing the data key from the JSON

        uid_found=0

        for i in data:
            #checking for the desired team and whether the match has started or not
            if(i['team-1'] == 'England' or i['team-2'] == 'England' and  i[matchStarted]):

                #getting todays date using datetime module     and      converting into Format: "%Y-%m-%d"
                #today = datetime.today().strftime('%Y-%m-%d')        -->as today i had no match i used some random time for trial of code
                today = '2020-08-05'

                #checking if the match occurs today
                if(today == i['date'].split("T")[0]):
                    uid_found=1       #If matches found: we flag it to 1
                    self.unique_id=i['unique_id']
                    print(self.unique_id)
                    break


        #If no matches found: we flag it to -1
        if not uid_found:
            self.unique_id=-1

        #getting the score for a match unique_id
        send_data=self.get_score(self.unique_id)

        #return the score data
        return send_data


#---------------------------------------------------------------------------------------------------------------------------------------------------------

#will fetch the score-details when it is given the unique_id
    def get_score(self, unique_id):
        data_raw = ""
        if unique_id==-1:
            data = "No Matches today"
        else:
            uri_params = {"apikey":self.api_key, "unique_id":unique_id}
            response = requests.get(self.url_get_score, params=uri_params)
            final_data = response.json()
            try:
                data = "Here's the match details:\n" + final_data['stat'] + "\n" + final_data['score']
            except Exception as e:
                print(e)

        return data


#---------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    match_obj=ScoreGet()
    whatsapp_message = match_obj.get_unique_id()
    #print(whatsapp_message)

    #Add the details from the DashBoard
    a_sid = "ACbfe4b9167845fa577c1288af9541f3c0"
    auth_token = "18e3b0adc8c6b80077bfea596304196c"
    client = Client(a_sid, auth_token)

    messages = client.messages.create(body=whatsapp_message, from_="whatsapp:+14155238886", to="whatsapp:+91 9939867080")
