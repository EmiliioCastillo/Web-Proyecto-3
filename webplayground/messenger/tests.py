from django.test import TestCase
from django.contrib.auth.models import User
from .models import Thread, Message

# Create your tests here.

class ThreadTestCase(TestCase):
    def SetUp(self):
        self.User1 = User.objects.create_user('user1', None, 'test1234')
        self.User2 = User.objects.create_user('user2', None , 'test1234')

        self.thread = Thread.objects.create()

    def test_add_users_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        self.assertEqual(len(self.thread.user_all()),2)

    def test_filter_thread_by_users(self):
        self.thread.users.add(self.user1, self.user2)
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(self.thread, threads[0])

    def test_filter_non_existent_thread(self):
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(len(threads),0)

    def test_add_messages_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1 = message.objects.create(users=user1, content="Hola")
        message2 = message.objects.create(users=user2, content="chau")
        self.thread.message.add(message1, message2)
        self.assertEqual(len(self.thread.message.all()), 2)
            
        for message in self.thread.message.all():
            print("{}:{}".format(message.user, message.content))
        
    def test_add_message_from_user_not_in_thread(self):
        self.thread.users.add(self.user1, self.user2, self.user3)
        message1 = message.objects.create(users=user1, content="Hola")
        message2 = message.objects.create(users=user2, content="chau")
        message2 = message.objects.create(users=user2, content="chau")
        self.thread.message.add(message1, message2, message3)
        self.assertEqual(len(self.thread.message.all()), 2)


    def test_find_thread_with_custom_manager(self):
        self.thread.users.add(self.user1, self.user2)
        threads = thread.objects.find(self.user1, self.user2)
        self.assertEqual(self.thread, thread)

    def test_find_or_create_thread_with_custom_manager(self):
         self.thread.users.add(self.user1, self.user2)
        thread = Thread.objects.find_or_create(self.user1, self.user2)
        self.assertEqual(self.thread, thread)
        thread = Thread.objects.find_or_create(self.user1, self.user3)
        self.assertIsNone(thread)




         
