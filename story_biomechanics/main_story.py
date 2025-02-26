
import os
import time
import webbrowser
import json

class Person:
    def __init__(self, name = "Sample", personality = "Anxious", attitude = "Negative"):
        self.name = name
        self.personality = personality # Anxious, Confident, Neutral
        self.attitude = attitude # Positive, Negative, Neutral
        self.reflecion_stage = 0
        self.house = None
        self.am_good = self.am_I_good_enough()
        self.need_good = self.need_to_be_good_enough()
        
        # Personal data
        self.nationality = None
        self.happiness = 0
        self.health = 100
        self.job = None
        self.gender = None
        self.sexual_orientation = None
        self.age = None
        self.education = None
        self.relationship_status = None
        self.political_views = None
        self.religion = None
        self.interests = []
        self.skills = []
        self.languages = []
        self.fears = []
        self.dreams = []
        self.goals = []
        self.hobbies = []
        self.friends = []
        
        # save person in people.json
        self.story_path = os.path.dirname(__file__)
        json_path = os.path.join(self.story_path, 'people.json')
        try:
            with open(json_path, 'r') as f:
                people = json.load(f)
        except FileNotFoundError:
            people = []
        except json.JSONDecodeError:
            people = []
            
        people.append(self.__dict__)
        
        # remove duplicates by comparing names and nationalities
        unique_people = { (each['name']) : each for each in people }.values()
        
        with open(json_path, 'w') as f:
            import pdb; pdb.set_trace()
            json.dump(unique_people, f)
        

    def reflect(self):
        print("Reflecting...")
        time.sleep(1)
        self.reflecion_stage += 1
    
    def make_decision(self, decision = "Answer"):
        
        start_time = time.time()
        decision_made = False
        print("Making a decision...")
        time.sleep(1)
        
        if self.should_I_do_it():
            print("Yes, you should do it!")
            print(f'{self.name} is making a decision: {decision}')
            print('\033[92mDecision made!\033[0m')
            decision_made = True
        else:
            print('\033[91mNo, you shouldn\'t do it!\033[0m')
            decision_made = False
            time.sleep(1)
            
        
        print("Time taken to make the decision: ", time.time() - start_time)
        print('\n')
        return decision_made
    
    def am_I_good_enough(self):
        if self.personality == "Anxious":
            self.am_good = False
            print("I'm not good enough!")
        elif self.personality == "Confident":
            self.am_good = True
            print("I'm good enough!")
        else:
            print("I'm not good enough!")
            
            while self.reflecion_stage < 5:
                self.reflect()
                
            self.am_good = True
            print("I'm good enough!")
        
    def need_to_be_good_enough(self):
        if self.personality == "Anxious":
            self.need_good = True
            print("I need to be good enough!")
            
        elif self.personality == "Confident":
            self.need_good = False
            print("I don't need to be good enough!")
            
        else:
            self.need_good = True
            print("I don't need to be good enough!")
        
    def should_I_do_it(self):
        
        self.am_I_good_enough()
        self.need_to_be_good_enough()
        
        if self.am_good and self.need_good == False: # Good enough + NOT need to be good enough (TRUE)
            return True
        elif self.am_good and self.need_good: # Good enough + Need to be good enough (TRUE)
            return True 
        elif not self.am_good and self.need_good: # NOT good enough + Need to be good enough (FALSE)
            print("No, you shouldn't do it!")
            print("You are not good enough!")
            return False
        elif not self.am_good and not self.need_good: # NOT good enough + NOT need to be good enough (TRUE)
            return True
        else:
            return "No, you shouldn't do it!"
        
    def update_personality(self):
        
        if self.house == None:
            print("No house assigned yet!")
            print("Personality remails: " + self.personality)
            return
        
        house_occupants = self.house.ocupant_names
        if self.name == "Miriam" and house_occupants == ["Miriam", "Bas"]:
            self.personality = "Confident"   
            print('\n')
            print('\033[95mMiriam loved moving in with Bas!\033[0m')
            print(f'{self.name} has a new personality: {self.personality}')   
            
class House:
    def __init__(self, name = "Sample House", location = "Sample Location", price = 0, occupants = []):
        self.name = name
        self.location = location
        self.price = price
        self.state = 'New'
        self.occupants = occupants
        self.ocupant_names = self.ocupants_names()
        if location == "Tel Aviv":
            self.link = 'https://www.properstar.co.uk/listing/100839370'
        else:
            self.link = 'https://www.youtube.com/watch?v=xvFZjo5PgG0'
        
        for occupant in occupants:
            occupant.house = self

        print('\n')
        print(f'House \033[94m{self.name}\033[0m created in \033[94m{self.location}\033[0m')
        print(f'House price: \033[94m{self.price}\033[0m')
        print(f'House occupants: \033[94m{self.ocupant_names}\033[0m')
    
    def ocupants_names(self):
        return [occupant.name for occupant in self.occupants]
    
    def show_link(self):
        print(f'House link: {self.link}')
        webbrowser.open(self.link)

class Story:
    
    class Section:
        def __init__(self, id='next', story=None, name='Template'):
            if not isinstance(story, Story):
                raise TypeError("story must be an instance of Story")
            
            # Section attributes
            self.story = story
            if id == 'next':
                self.id = len(story.sections) + 1
            self.name = name
            self.text = story.section_text(self.id)
            self.characters = []
                   
        def print(self):
            print('\n')
            print(self.text)
            
    def add_section(self, text):
        self.sections.append(self.Section(story=self, text=text))
            
    # Story         
    def __init__(self, id=1):
        if id == 1:
            
            Miriam = Person(name = "Miriam", personality = "Anxious", attitude = "Negative")
            Bas = Person(name = "Bas", personality = "Confident", attitude = "Positive")
            
            self.character_1 = Miriam
            self.character_2 = Bas
            
            self.sections = list(range(1, 11))  # create 10 sections 
            self.sections[1] = self.Section(id=1, story=self, name='Introduction')
            self.sections[2] = self.Section(id=2, story=self, name='Chapter 1')
            self.sections[3] = self.Section(id=3, story=self, name='Chapter 2')
                        
            
        else:
            print("No story available!")
    
    def add_person(self, person):
        if isinstance(person, Person):
            raise TypeError("person must be an instance of Person")
        
        self.sections[-1].characters = person
    
    def plots(self, section_number):
        if self.id == 1:
            if section_number == 3:
                decision_made = False   
                while decision_made == False:
                    
                    answer = input("Want to make a decision? (Enter to continue)")
                    
                    if answer == "Move in with Bas" or answer == None:
                        ocuppants = [self.character_1, self.character_2]
                        H = House(name = "Fartville", location = "Tel Aviv", price = 1000, occupants = ocuppants)
                        self.character_1.update_personality()
                    else:
                        self.character_1.make_decision()

                input("Do you like to see Miriam and Bas's house? Press Enter to continue...")
                H.show_link()
                return True
            else:
                return False
        
        
    def section_text(self, section_number):
        
        if self.id == 1:
            if section_number == 1:
                text = f"{self.character_1.name} and {self.character_2.name} are two muppets living in Vienna"
                
            elif section_number == 2:
                text = f"{self.character_1.name} is not good at making decisions"
                
            elif section_number == 3:
                text = f"{self.character_1.name} and {self.character_2.name} love to live together in but the there is a lot of tension"
                
        return text
    
    def print_section(self, section_id):
        print('\n')
        print(self.sections[section_id].text)
        
        
if __name__ == "__main__":
    
    
    # basics
    P = Person(name = "Miriam", personality = "Anxious", attitude = "Negative") # create a person
    P2 = Person(name = "Bas", personality = "Confident", attitude = "Positive") # create a person
    
    
    
    # select the story
    S = Story(id=1)
    
    # section 1
    S.print_section(1)
    
    # section 2 - Bas and Miriam move in together
    S.print_section(2)
   
    # Section 3 - Tel Aviv gets attacked by Iran
    input("Do you like your new house? Press Enter to continue the story...")    
    
    # Section 4 - Bas and Miriam move in together