import re
import long_responses as long
import webbrowser


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Welcome to HealthPal, how may I help you?\n Select from the options below :\n Press 1 - Track my periods \n Press 2 - Symptom Diagnosis \n Press 3 - Find a Doctor \n Press 4 - Diet/Lifestyle Recommendations', ['hello', 'hi', 'hey', 'sup', 'heyo','heya','Namaste'], single_response=True)
    response('Glad to hear from you, See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('Proceed to the link to track your periods : https://flo.health/', ['1', 'one'], single_response=True)
    response('Enter the symptoms you are facing.', ['2', 'two'], single_response=True)
    response('What do you prefer?\n Online consultation (Enter \'a\')\n Doctors nearby (Enter \'b\')', ['3', 'three'], single_response=True)
    response('Follow the chart below :\n https://food.ndtv.com/food-drinks/balanced-diet-a-complete-guide-to-healthy-eating-2037559', ['4', 'four'], single_response=True)
    response('Enter the symptoms you have.', ['a', 'A'], single_response=True)
    response('Book a consultation now : https://www.practo.com/bangalore/doctors', ['b', 'B'], single_response=True)
    response('Viral infection!...Consult a doctor : https://www.practo.com/consult', ['headache', 'fever','cough', 'cold','sore','throat'], single_response=True)
    response('Hormonal imbalance!...See a Dermatologist : https://www.practo.com/consult', ['pimples','acne', 'zits','blackheads','spot','spots','pigmentation','pores'], single_response=True)
    response('Microbial infection, better to get medicines before it spreads: https://www.practo.com/consult', ['rashes', 'fungal','infection', 'rings','itching','itch','dark'], single_response=True)

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('HealthBot: ' + get_response(input('You: ')))
