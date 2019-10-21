class User:

    def __init__(self,first,last,bio,position,company,ID,password):
        self.first = first
        self.last = last
        self.bio = bio
        self.position = position
        self.company = company
        self.email = first + '.' + last + '@' + company + '.com'
        self.ID = ID
        self.password = password

    def fullname(self):
        return '{} {}' .format(self.first, self.last)