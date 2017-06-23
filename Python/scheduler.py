class Student:
	def __init__(self, id, status = False):
		self.id = id
		self.status = status 	#False status means it is yet to be assigned to an interview (ie. it is free)
								#same logic throughout the code

class Room:
	def __init__(self, id, durations_list):
		self.id = id
		self.status_dict = dict()

		#for each duration, set the room available

		for duration in durations_list:
			self.status_dict[duration] = False

class Interviewer:
	def __init__(self, id, durations_list):
		self.id = id
		self.status_dict = dict()

		#for each duration, set the interviewer available
		for duration in durations_list:
			self.status_dict[duration] = False

class Interview:
	def __init__(self, id):
		self.id = id
		self.student = None
		self.interviewer = None
		self.duration = None
		self.room = None

class Duration:
	def __init__(self, start, day):
		self.start = start
		self.end = start+2
		self.day = day

class Scheduler:

	def __init__(self, no_students, no_interviewers, no_rooms):
		#store the list of duration objects
		self.day = 1
		self.durations_list = []

		#if day one is not enough for conducting all the interviews, then add more durations for the next day
		while(no_interviewers*len(self.durations_list) < no_students):			
			self.durations_list.extend([Duration(8, self.day), Duration(10, self.day), Duration(13, self.day), Duration(15, self.day), Duration(17, self.day)])
			self.day += 1

		#store a list of objects for: room, interviewer, student, interviewer (number of objects as inputed by the user)
		self.rooms_list = [Room(no, self.durations_list) for no in range(1, no_rooms+1)]
		self.interviewers_list = [Interviewer(no, self.durations_list) for no in range(1, no_interviewers+1)]
		self.students_list = [Student(no) for no in range(1, no_students+1)]
		self.interviews_list = [Interview(no) for no in range(1, no_students+1)]

		#until every student is assigned an interview:
		for current_interview in self.interviews_list:	
			#assign a free student to it
			current_interview.student = self.get_a_free_student()

			#for the same duration: assign a free interviewer and a free room free at that interval	
			self.assign_duration_room_interviewer(current_interview)

		self.show_schedule()

	#take any student who is free
	def get_a_free_student(self):
		for student in self.students_list:
			if(student.status == False):
				student.status = True
				return student

	#choose a room and an interviewer who are both free for a particular duration
	def assign_duration_room_interviewer(self, current_interview):
		for duration in self.durations_list:
			for interviewer in self.interviewers_list:
				for room in self.rooms_list:
					#if both the room and the interviewer are free (ie status is false for that duration)
					if(not room.status_dict[duration] and not interviewer.status_dict[duration] ):
						#assign them to the current interview
						current_interview.interviewer = interviewer
						current_interview.room = room
						current_interview.duration = duration

						#set room and the interviewer as not available (set the status as True)
						room.status_dict[duration] = True
						interviewer.status_dict[duration] = True
						return

	#prints the solution
	def show_schedule(self):
		print("\nHere's the schedule: \n")
		print("  ******************************************************************************************")
		print("\tStudent\t\tRoom\t\tDay\t\tDuration\t\tInterviewer")
		print("  ******************************************************************************************")
		for interview in self.interviews_list:
			print("\t" + str(interview.student.id) + "\t\t" + str(interview.room.id) + "\t\t" + str(interview.duration.day) + "\t\t" + str(interview.duration.start).rjust(2, '0') + " to " + str(interview.duration.end).rjust(2, '0') + "\t\t" + str(interview.interviewer.id))

		print("  ******************************************************************************************")


#the execution starts here
choice = 'y'
print("\n*********  The Interview Scheduler  *********")

while(choice == 'y' or choice == 'Y'):
	print("\n")
	no_students = int(input("Enter no of students: "))
	no_rooms = int(input("Enter no of rooms: "))
	no_interviewers = int(input("Enter no of interviewers: "))

	Scheduler(no_students, no_interviewers, no_rooms)	

	choice = input("\n\nAnother input?(y/n): ")



