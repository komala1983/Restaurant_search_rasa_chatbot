## Generated Story -2104916557826241612
* greet{"location": "hola"}
    - slot{"location": "hola"}
    - utter_greet
* restaurant_search{"location": "varanasi"}
    - slot{"location": "varanasi"}
    - action_verify_location
    - slot{"location": "varanasi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
	- action_verify_budget
    - slot{"price": "1"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* affirm
    - utter_ask_email
* emailId
    - action_verify_email
    - slot{"email": null}
* emailId
    - action_verify_email
    - slot{"email": null}
* emailId{"email": "ankitpandey.it@gmail.com"}
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_verify_email
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - export

## Generated Story -659809807787252498
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "maihar"}
    - slot{"location": "maihar"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "katni"}
    - slot{"location": "katni"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "patna"}
    - slot{"location": "patna"}
    - action_verify_location
    - slot{"location": "patna"}
	- utter_ask_budget
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
	- action_verify_budget
    - slot{"price": "3"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* affirm
    - utter_ask_email
* emailId
    - action_verify_email
    - slot{"email": null}
* emailId
    - action_verify_email
    - slot{"email": null}
* emailId{"email": "ankitpandey.it@gmail.com"}
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_verify_email
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - export

## Generated Story 7785980985154205470
* restaurant_search{"cuisine": "north indian", "location": "pune"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "pune"}
    - action_verify_location
    - slot{"location": "pune"}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
	- utter_ask_budget
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
	- action_verify_budget
    - slot{"price": "3"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export
	
## Generated Story 5032413632475528881
* restaurant_search{"location": "varanasi"}
    - slot{"location": "varanasi"}
    - action_verify_location
    - slot{"location": "varanasi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
	- utter_ask_budget
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
	- action_verify_budget
    - slot{"price": "3"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* affirm
    - utter_ask_email
* emailId{"email": "ankitp@yahoo.co.in"}
    - slot{"email": "ankitp@yahoo.co.in"}
	- action_verify_email
	- slot{"email": "ankitp@yahoo.co.in"}
	- action_send_email
    - export
	
## Generated Story 5032413632475528883
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_verify_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
	- utter_ask_budget
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
	- action_verify_budget
    - slot{"price": "2"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* affirm
    - utter_ask_email
* emailId{"email": "ankitpandey.it@gmail.com"}
    - slot{"email": "ankitpandey.it@gmail.com"}
	- action_verify_email
	- slot{"email": "ankitpandey.it@gmail.com"}
	- action_send_email
    - export

## Generated Story 6631058235073708738
* greet{"location": "hola"}
    - slot{"location": "hola"}
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "delhi"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "delhi"}
    - action_verify_location
    - slot{"location": "delhi"}
    - action_verify_cuisine
    - slot{"cuisine": "mexican"}
	- utter_ask_budget
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
	- action_verify_budget
    - slot{"price": "1"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* affirm
    - utter_ask_email
* emailId
    - action_verify_email
    - slot{"email": null}
    - utter_ask_email
* emailId{"email": "ankitpandey.it@gmail.com"}
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_verify_email
    - action_send_email
	- utter_send_email_confirm
    - export


## Generated Story 3526190785627510104
* restaurant_search{"cuisine": "north indian", "location": "mumbai"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "mumbai"}
    - action_verify_location
    - slot{"location": "mumbai"}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
	- utter_ask_budget
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
	- action_verify_budget
    - slot{"price": "2"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* emailId{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - action_verify_email
    - slot{"email": "xyz@sth.edu"}
    - action_send_email
    - reset_slots
    - export
	
## Generated Story 904058040013094472
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search
    - action_verify_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
	- action_verify_budget
    - slot{"price": "2"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* goodbye
    - utter_goodbye
	- action_slot_reset
    - reset_slots
    - export

## Generated Story -7275210863371988889
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_verify_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
	- utter_ask_budget
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
	- action_verify_budget
    - slot{"price": "2"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* emailId{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - action_verify_email
    - slot{"email": "xyz@sth.edu"}
    - action_send_email
    - reset_slots
    - export

## Generated Story -7787685597116754311
* restaurant_search
    - utter_ask_location
* emailId{"location": "mathura"}
    - slot{"location": "mathura"}
    - action_verify_location
    - slot{"location": "mathura"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
	- utter_ask_budget
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
	- action_verify_budget
    - slot{"price": "2"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* affirm
    - utter_ask_email
* emailId{"email": "ankitpandey.it@gmail.com"}
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_verify_email
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_send_email
    - utter_send_email_confirm
    - action_slot_reset
    - reset_slots
    - export

## Generated Story -4829169260985836983
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "lucknow"}
    - slot{"location": "lucknow"}
    - action_verify_location
	- slot{"location": "lucknow"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_verify_cuisine
    - slot{"cuisine": "italian"}
	- utter_ask_budget
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
	- action_verify_budget
    - slot{"price": "1"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* goodbye
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export

## Generated Story -8426370142091287284
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "indore"}
    - slot{"location": "indore"}
    - action_verify_location
    - slot{"location": "indore"}
	- utter_ask_budget
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
	- action_verify_budget
    - slot{"price": "2"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* affirm
    - utter_ask_email
* emailId{"email": "ankitpandey.it@gmail.com"}
    - slot{"email": "ankitpandey.it@gmail.com"}
	- action_verify_email
	- slot{"email": "ankitpandey.it@gmail.com"}
    - action_send_email
    - utter_send_email_confirm
    - action_slot_reset
    - reset_slots
    - export

## Generated Story -6723606267445830870
* restaurant_search{"cuisine": "american", "location": "gandhinagar"}
    - slot{"cuisine": "american"}
    - slot{"location": "gandhinagar"}
    - action_verify_location
    - slot{"location": null}
    - action_verify_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_verify_location
    - slot{"location": "mumbai"}
	- utter_ask_budget
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
	- action_verify_budget
    - slot{"price": "2"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* goodbye
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export

## Generated Story -4596885303222705549
* 
    - utter_default
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export

## Generated Story -7759872241478167142
* not_interested
    - utter_default
* not_interested
    - utter_default
* not_interested
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export

## Generated Story -2865052614806521958
* not_interested
    - utter_default
* emailId
    - utter_default
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangaloree"}
    - slot{"location": "bangaloree"}
    - action_verify_location
    - slot{"location": null}
	- utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
	- action_verify_budget
    - slot{"price": "2"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* goodbye
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export

## Generated Story 302309814264637075
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_verify_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
	- action_verify_budget
    - slot{"price": "2"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* goodbye
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export

## Generated Story -4823550431509858117
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
	- action_verify_budget
    - slot{"price": "2"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export

## Generated Story -4843119173524996953
* restaurant_search{"cuisine": "chinese", "location": "bangalore", "price": "2"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - slot{"price": "2"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
	- action_verify_budget
    - slot{"price": "2"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* affirm
    - utter_ask_email
* emailId
    - action_verify_email
    - slot{"email": null}
    - utter_ask_email
* emailId{"email": "ankitpandey.it@yahoo.co.in"}
    - slot{"email": "ankitpandey.it@yahoo.co.in"}
    - action_verify_email
    - slot{"email": "ankitpandey.it@yahoo.co.in"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export

## Generated Story 3487104430574389001
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - utter_ask_budget
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - action_verify_budget
    - slot{"price": "1"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export

## Generated Story -206462978309641752
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_verify_cuisine
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
	- action_verify_budget
    - slot{"price": "2"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* affirm
    - utter_ask_email
* emailId
    - action_verify_email
    - slot{"email": null}
* emailId
    - action_verify_email
    - slot{"email": null}
* emailId{"email": "ankitpandey.it@gmail.com"}
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_verify_email
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - export

## Generated Story -2239276814112331622
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_verify_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_verify_cuisine
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
	- action_verify_budget
    - slot{"price": "2"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export

## Generated Story -53498501491139177
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
	- action_verify_budget
    - slot{"price": "3"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export

## Generated Story 5128086029905420137
* restaurant_search{"cuisine": "indian"}
    - slot{"cuisine": "indian"}
    - action_verify_cuisine
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "north indian", "location": "Mumbai"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location": "Mumbai"}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_verify_budget
    - slot{"price": "3"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export

## Generated Story -424294329870064066
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_verify_location
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_verify_budget
    - slot{"price": "2"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* emailId{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export
	
## Generated Story -4625703641335565640
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_verify_location
    - slot{"location": "allahabad"}
    - utter_ask_cuisine
* restaurant_search
    - action_verify_cuisine
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_verify_budget
    - slot{"price": "3"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* emailId
    - action_verify_email
    - slot{"email": null}
* emailId
    - action_verify_email
    - slot{"email": null}
* emailId{"email": "ankitpandey@upgrad.com"}
    - slot{"email": "ankitpandey@upgrad.com"}
    - action_verify_email
    - slot{"email": "ankitpandey@upgrad.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - export

## Generated Story 2055400917469852318
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_verify_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - action_verify_budget
    - slot{"price": "1"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* affirm
    - utter_ask_email
* emailId{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_verify_email
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_send_email
    - reset_slots
    - action_slot_reset
    - reset_slots
    - export

## Generated Story 1203253057029578553
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_verify_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_verify_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - action_verify_budget
    - slot{"price": "1"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export

## Generated Story 7677165091880445876
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "<  300"}
    - slot{"price": "<  300"}
    - action_verify_budget
    - slot{"price": null}
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export
	
## Generated Story -8644060774145208518
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - action_verify_budget
    - slot{"price": "1"}
	- action_verify_slots
    - action_restaurant
    - slot{"price": null}
    - action_verify_slots
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* affirm
    - utter_ask_email
* emailId{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - action_verify_email
    - slot{"email": "xyz@sth.edu"}
    - action_send_email
    - reset_slots
    - action_slot_reset
    - reset_slots
    - export

## Generated Story 6677082117145452495
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Bangalore"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Bangalore"}
    - action_verify_location
    - slot{"location": "Bangalore"}
    - action_verify_cuisine
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - action_verify_budget
    - slot{"price": "1"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export

## Generated Story 2710853297708227371
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Bangalore"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Bangalore"}
    - action_verify_location
    - slot{"location": "Bangalore"}
    - action_verify_cuisine
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - action_verify_budget
    - slot{"price": "1"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export

## Generated Story 4809260142745259489
* greet
    - utter_greet
* restaurant_search{"location": "mumbai", "cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_verify_location
    - slot{"location": "mumbai"}
    - action_verify_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - action_verify_budget
    - slot{"price": "1"}
	- action_verify_slots
    - action_restaurant
    - slot{"price": null}
    - action_verify_slots
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export
	
## Generated Story -7542212843689219461
* greet
    - utter_greet
* restaurant_search{"location": "mumbai", "cuisine": "italian", "price": "1"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
	- slot{"price": "1"}
    - action_verify_location
    - slot{"location": "mumbai"}
    - action_verify_cuisine
    - slot{"cuisine": "italian"}
	- action_verify_budget
    - slot{"price": "1"}
    - action_restaurant
    - slot{"price": null}
    - action_verify_slots
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
	- action_verify_slots
    - action_restaurant
	- action_verify_slots
    - utter_ask_send_email
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export
	
## Generated Story 2653783219795394363
* restaurant_search{"cuisine": "italian", "location": "Mumbai", "price": "1"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Mumbai"}
    - slot{"price": "1"}
    - action_verify_location
    - slot{"location": "Mumbai"}
    - action_verify_cuisine
    - slot{"cuisine": "italian"}
    - action_verify_budget
    - slot{"price": "1"}
    - action_restaurant
    - slot{"price": null}
    - action_verify_slots
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - action_restaurant
    - slot{"price": null}
    - action_verify_slots
* restaurant_search{"price": "> 300"}
    - slot{"price": "> 300"}
    - action_verify_budget
    - slot{"price": null}
    - utter_ask_budget
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_verify_budget
    - slot{"price": "2"}
	- action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* emailId{"email": "ankitan@gmail.com"}
    - slot{"email": "ankitan@gmail.com"}
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export

## Generated Story -2945158319018838346
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bangalore"}
    - action_verify_location
    - slot{"location": "Bangalore"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_verify_budget
    - slot{"price": "3"}
	- action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* emailId{"email": "ankitpandey.it@gmail.com"}
    - slot{"email": "ankitpandey.it@gmail.com"}
    - utter_send_email_confirm
    - action_slot_reset
    - reset_slots
    - export

## Generated Story 5551688847517788752
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_verify_budget
    - slot{"price": "3"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* emailId{"email": "ankitpandey.it@gmail.com"}
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_send_email
    - action_slot_reset
    - reset_slots
    - export
	
## Generated Story 5103699314780100904
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "varanasi"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "varanasi"}
    - action_verify_location
    - slot{"location": "varanasi"}
    - action_verify_cuisine
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_verify_budget
    - slot{"price": "3"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* affirm
    - utter_ask_email
* emailId{"email": "ankitpandey.it@gmail.com"}
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_verify_email
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_send_email
    - utter_send_email_confirm
    - action_slot_reset
    - reset_slots
    - export

## Generated Story -5738816255482932016
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mathura"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mathura"}
    - action_verify_location
    - slot{"location": "mathura"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_verify_budget
    - slot{"price": "3"}
    - action_verify_slots
    - action_restaurant
    - slot{"price": null}
    - action_verify_slots
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* affirm
    - utter_ask_email
* emailId{"email": "ankitpandey.it@gmail.com"}
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_verify_email
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_send_email
    - reset_slots
    - export

## Generated Story 8632023896535045754
* greet
    - utter_greet
* restaurant_search{"location": "salem"}
    - slot{"location": "salem"}
    - action_verify_location
    - slot{"location": "salem"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_verify_budget
    - slot{"price": "2"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export

## Generated Story -3959815890000182282
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "salem"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "salem"}
    - action_verify_location
    - slot{"location": "salem"}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_verify_budget
    - slot{"price": "2"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* affirm
    - utter_ask_email
* emailId{"email": "vinijai89@gmail.com"}
    - slot{"email": "vinijai89@gmail.com"}
    - action_verify_email
    - slot{"email": "vinijai89@gmail.com"}
    - action_send_email
    - reset_slots
    - export

## Generated Story -6763828335842991993
* restaurant_search{"cuisine": "chinese", "location": "mumbai", "price": "3"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - slot{"price": "3"}
    - action_verify_location
    - slot{"location": "mumbai"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - action_verify_budget
    - slot{"price": "3"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* emailId{"email": "ankitpandey.it@gmail.com"}
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_send_email
    - reset_slots
    - export

## Generated Story -7666936227444476953
* restaurant_search{"cuisine": "north indian", "location": "bengalore"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "bengalore"}
    - action_verify_location
    - slot{"location": null}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_verify_budget
    - slot{"price": "3"}
    - action_verify_slots
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* emailId{"email": "alokpandey.it@gmail.com"}
    - slot{"email": "alokpandey.it@gmail.com"}
    - action_send_email
    - reset_slots
    - export

## Generated Story -19205096620656192
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_verify_location
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_verify_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search
    - action_verify_budget
    - slot{"price": null}
    - action_verify_slots
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* emailId{"email": "ankitpandey.it@gmail.com"}
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_send_email
    - reset_slots
    - export

## Generated Story 4166533707059151784
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* emailId
    - action_verify_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - utter_ask_budget
* restaurant_search{"price": "400 to 600"}
    - slot{"price": "400 to 600"}
    - action_verify_budget
    - slot{"price": null}
    - action_verify_slots
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* emailId{"email": "ankitpandey.it@gmail.com"}
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_send_email
    - reset_slots
    - export

## Generated Story -5525459303534777809
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search
    - action_verify_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_verify_location
    - slot{"location": "pune"}
    - utter_ask_budget
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_verify_budget
    - slot{"price": "2"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* emailId{"email": "ankitpandey.it@gmail.com"}
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_send_email
    - reset_slots
    - export

## Generated Story -8826105988432044864
* restaurant_search{"cuisine": "north indian", "location": "mysuru"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "mysuru"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "mysore"}
    - slot{"location": "mysore"}
    - action_verify_location
    - slot{"location": "mysore"}
    - utter_ask_budget
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_verify_budget
    - slot{"price": "2"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* emailId{"email": "ankitpandey.it@gmail.com"}
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_send_email
    - reset_slots
    - export


## Generated Story 8583233470921333680
* restaurant_search{"location": "mysuru"}
    - slot{"location": "mysuru"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "mysore"}
    - slot{"location": "mysore"}
    - action_verify_location
    - slot{"location": "mysore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_verify_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_verify_budget
    - slot{"price": "3"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* emailId{"email": "ankitpandey.it@gmail.com"}
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_send_email
    - reset_slots
    - export

## Generated Story -5265168917689126434
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_verify_location
    - slot{"location": "allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_verify_budget
    - slot{"price": "3"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* affirm
    - utter_ask_email
* emailId{"email": "ankitpandey.it@gmail.com"}
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_verify_email
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_send_email
    - reset_slots
    - export

## Generated Story 8921996374286770940
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_verify_location
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_verify_budget
    - slot{"price": "3"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* emailId{"email": "ankitpaney.it@gmail.com"}
    - slot{"email": "ankitpaney.it@gmail.com"}
    - action_send_email
    - reset_slots
    - export

## Generated Story 1733169307106391596
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_verify_location
    - slot{"location": "chandigarh"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - action_verify_budget
    - slot{"price": "1"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export

## Generated Story -5832656281639878311
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_verify_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - action_verify_budget
    - slot{"price": "1"}
    - action_verify_slots
    - action_restaurant
    - slot{"price": null}
    - action_verify_slots
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* affirm
    - utter_ask_email
* emailId{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_verify_email
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_send_email
    - reset_slots
    - export

## Generated Story 8297236844760752772
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_verify_budget
    - slot{"price": "3"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* affirm
    - utter_ask_email
* emailId{"email": "ankitpandey.it@gmail.com"}
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_verify_email
    - slot{"email": "ankitpandey.it@gmail.com"}
    - action_send_email
    - reset_slots
    - export

## Generated Story 7170522706920843239
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_verify_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - action_verify_budget
    - slot{"price": "1"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* affirm
    - utter_ask_email
* emailId{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_verify_email
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_send_email
    - reset_slots
    - export

## Generated Story -4205349748376245904
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_verify_location
    - slot{"location": "allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_verify_budget
    - slot{"price": "3"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* emailId{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - action_verify_email
    - slot{"email": "xyz@sth.edu"}
    - action_send_email
    - reset_slots
    - export

## Generated Story 4765351690802010563
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_verify_budget
    - slot{"price": "2"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* emailId{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_verify_email
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - reset_slots
    - export

## Generated Story 5786587044921140224
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_verify_location
    - slot{"location": "chandigarh"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - action_verify_budget
    - slot{"price": "1"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - export

## Generated Story -6853506319182006127
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_verify_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - action_verify_budget
    - slot{"price": "1"}
    - action_verify_slots
    - action_restaurant
    - slot{"price": null}
    - action_verify_slots
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* affirm
    - utter_ask_email
* emailId{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_verify_email
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_send_email
    - reset_slots
    - export

## Generated Story -3421120858911993165
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "varanasi"}
    - slot{"location": "varanasi"}
    - action_verify_location
    - slot{"location": "varanasi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_verify_budget
    - slot{"price": "3"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* emailId{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - action_verify_email
    - slot{"email": "xyz@sth.edu"}
    - action_send_email
    - reset_slots
    - export

## Generated Story 7686232543326936286
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "varanasi"}
    - slot{"location": "varanasi"}
    - action_verify_location
    - slot{"location": "varanasi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_verify_budget
    - slot{"price": "3"}
    - action_verify_slots
    - action_restaurant
    - action_verify_slots
    - utter_ask_send_email
* emailId{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - action_verify_email
    - slot{"email": "xyz@sth.edu"}
    - action_send_email
    - reset_slots
    - export

