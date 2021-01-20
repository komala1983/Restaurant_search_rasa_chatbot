from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
from rasa_core.events import AllSlotsReset
from rasa_core.events import Restarted

import re
import smtplib
import pandas as pd
from email.message import EmailMessage



config={ "user_key":"1d1314ef0234d736b96d8b9e93844836"} #Enter Zomato API key
global messageToSend
messageToSend = ""

class ActionVerifyLocation(Action):
	def name(self):
		return 'action_verify_location'
		
	def run(self, dispatcher, tracker, domain):
		
		tier_1_2 = ["ahmedabad","bangalore","chennai","delhi","hyderabad","kolkata","mumbai","pune","agra","ajmer","aligarh","allahabad","amravati","amritsar",
					"asansol","aurangabad","bareilly","belgaum","bhavnagar","bhiwandi","bhopal","bhubaneswar","bikaner","bokaro steel city","chandigarh","coimbatore","cuttack","dehradun","dhanbad","durg-bhilai nagar","durgapur","erode","faridabad","firozabad","ghaziabad","gorakhpur","gulbarga","guntur","gurgaon","guwahati","gwalior","hubli-dharwad","indore","jabalpur","jaipur","jalandhar","jammu","jamnagar","jamshedpur","jhansi","jodhpur","kannur","kanpur","kakinada","kochi","kottayam","kolhapur","kollam","kota","kozhikode","kurnool","lucknow","ludhiana","madurai","malappuram","mathura","goa","mangalore","meerut","moradabad","mysore","nagpur","nanded","nashik","nellore","noida","palakkad","patna","pondicherry","raipur","rajkot","rajahmundry","ranchi","rourkela","salem","sangli","siliguri","solapur","srinagar","sultanpur","surat","thiruvananthapuram","thrissur","tiruchirappalli","tirunelveli","tiruppur","ujjain","vijayapura","vadodara","varanasi","vasai-virar city","warangal","vijayawada","visakhapatnam"]
		
		loc = tracker.get_slot('location')
		
		if loc is None:
			dispatcher.utter_template("utter_ask_location", tracker)
		else:
		
			if loc is not None:
				if loc.lower() in tier_1_2:
					return[SlotSet('location',loc)]
				else:
					dispatcher.utter_template("utter_location_not_found",tracker)
					return[SlotSet('location',None)]
			else:
				dispatcher.utter_message("Sorry I could not understand the location name you provided. Please try some other location")
				return[SlotSet('location',None)]


class ActionVerifyCuisine(Action):
	def name(self):
		return 'action_verify_cuisine'
		
	def run(self, dispatcher, tracker, domain):
		lst_cuisine = ["chinese","mexican","american","italian","south indian","north indian"]
		cus = tracker.get_slot('cuisine')
		if cus is not None:
			if cus.lower() in lst_cuisine:
				return[SlotSet('cuisine',cus)]
			else:
				dispatcher.utter_message("Sorry this is not a valid cuisine. please provide cuisine again.")
				return[SlotSet('cuisine',None)]
		else:
			dispatcher.utter_message("Sorry I could not understand the cuisine name you provided. Please choose cuisine from list provided.")
			return[SlotSet('cuisine', None)]			

class ActionVerifyEmail(Action):
	def name(self):
		return 'action_verify_email'
		
	def run(self, dispatcher, tracker, domain):
		pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
		email_id = tracker.get_slot('email')
		if email_id is not None:
			if re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",email_id):
				return[SlotSet('email',email_id)]
			else:
				dispatcher.utter_message("Sorry this is not a valid email. please try again")
				return[SlotSet('email',None)]
		else:
			dispatcher.utter_message("Sorry I could not understand the given email address, Please try again")
			return[SlotSet('email', None)]	

class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'
		
	def run(self, dispatcher, tracker, domain):
		global messageToSend
		email = tracker.get_slot('email')
		
		setup = smtplib.SMTP('smtp.gmail.com', 587) 
		setup.starttls() 
		setup.login("source email id", "password") #Provide Your Email Id and respective Password from which you want to send email.
		msg = EmailMessage()
		email_body = "Please find below top rated restaurants as requested: \n \n"
		email_body = email_body + messageToSend
		msg.set_content(email_body)
		msg['Subject'] = 'Search results from Foodie Bot'
		msg['From'] = 'source email id'   #Provide Your Email Id from which you want to send email.
		msg['To'] = email
		try:
			setup.send_message(msg)
			setup.quit()
			dispatcher.utter_template("utter_send_email_confirm", tracker)
		except:
			dispatcher.utter_message(email)

		messageToSend = ""
		return [AllSlotsReset()]


class ActionVerifyBudget(Action):
	def name(self):
		return 'action_verify_budget'
	
	def run(self, dispatcher, tracker, domain):
		budget=['1','2','3']
		price = tracker.get_slot('price')
		if price is not None:
			if price in budget:
				return[SlotSet('price',price)]
			else:
				dispatcher.utter_message("Sorry, we could not recognize provided price range.")
				return[SlotSet('price',None)]
		else:
			dispatcher.utter_message("Sorry, we could not recognize provided price range.")
			return[SlotSet('price', None)]		
			
class ActionVerifySlots(Action):
	def name(self):
		return 'action_verify_slots'
	
	def run(self, dispatcher, tracker, domain):
		price = tracker.get_slot('price')
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		if loc is not None:
			if cuisine is not None:
				if price is not None:
					pass
				else:
					dispatcher.utter_template("utter_ask_budget", tracker)
			else:
				dispatcher.utter_template("utter_ask_cuisine", tracker)
			
		else:
			dispatcher.utter_template("utter_ask_location", tracker)
			
class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		global messageToSend
		zomato = zomatopy.initialize_app(config)		
		loc = tracker.get_slot('location')
		loc = loc.lower()
		cuisine = tracker.get_slot('cuisine')
		cuisine = cuisine.lower()
		price = tracker.get_slot('price')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'chinese':25,'mexican':73,'italian':55,'american':1,'south indian':85,'north indian':50}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 20)
		if (price == '1'):
			range_min = 0
			range_max = 299
		elif (price == '2'):
			range_min = 300
			range_max = 700
		else:
			range_min = 701
			range_max = 10000
		
		d = json.loads(results)
		
		restaurant_df = pd.DataFrame(columns=['Restaurant Name','Restaurant locality address','Average budget for two people','Zomato user rating'])
		
		response=""
		email_msg = ""
		messageToSend = ""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				avg_cost_for_2 = restaurant['restaurant']['average_cost_for_two']
				if avg_cost_for_2 >= range_min and avg_cost_for_2 <= range_max:
					new_row = {'Restaurant Name':restaurant['restaurant']['name'],'Restaurant locality address':restaurant['restaurant']['location']['address'],'Average budget for two people':str(restaurant['restaurant']['average_cost_for_two']),'Zomato user rating':restaurant['restaurant']['user_rating']['aggregate_rating']}
					restaurant_df = restaurant_df.append(new_row, ignore_index=True)
		
		restaurant_df['Zomato user rating'] = restaurant_df['Zomato user rating'].astype(float)
		restaurant_df.sort_values(['Zomato user rating'], ascending = False, inplace=True)
		restaurant_df['Zomato user rating'] = restaurant_df['Zomato user rating'].astype(str)
		restaurant_df.reset_index(drop=True)
		
		if len(restaurant_df) != 0:
			if len(restaurant_df) <= 5:
				num_listings = len(restaurant_df)
			else:
				num_listings = 5
			for i in range(num_listings):
				response= response + restaurant_df.iloc[i,0] + " in " + restaurant_df.iloc[i,1] + " has been rated " + restaurant_df.iloc[i,3] + "\n"
			
			if len(restaurant_df) <= 10:
				num_listings = len(restaurant_df)
			else:
				num_listings = 10
			for i in range(num_listings):
				messageToSend = messageToSend + restaurant_df.iloc[i,0] + " in " + restaurant_df.iloc[i,1] + " with avg budget Rs. " + restaurant_df.iloc[i,2]  + " for two people "  + " has been rated " + restaurant_df.iloc[i,3] + "\n"
				
			dispatcher.utter_message("Showing you top rated restaurants: ")
			dispatcher.utter_message(response)
		else:
			dispatcher.utter_message("Found 0 restaurants for given price range and location, please try with higher range.")
			return [SlotSet('price',None)]

		
class ActionSlotReset(Action): 	
    def name(self): 		
        return 'action_slot_reset'
    def run(self, dispatcher, tracker, domain): 		
        return[AllSlotsReset()]
