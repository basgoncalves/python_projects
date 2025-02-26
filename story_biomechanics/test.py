class Story:
    
    class Section:
        def __init__(self, id='next', story=None, name='Template', text=None):
            if not isinstance(story, Story):
                raise TypeError("story must be an instance of Story")
            
            self.story = story
            if id == 'next':
                self.id = len(story.section) + 1
            self.name = name
            self.text = text
        
        def print(self):
            print('\n')
            print(self.text)
            
    def add_section(self, text):
        self.section.append(self.Section(story=self, text=text))
        
    def __init__(self, id=1):
        if id == 1:
            self.section = list(range(1, 11))  # create 10 sections 
            self.section[1] = self.Section(story=self, name='Introduction', text="Once upon a time in a far away land...")

s = Story(id=1)
s.section[1].print()