from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.
from links.schema import schema
from links.models import Link

LINKS_QUERY = '''
 {
   links {
     id
     url
     description
   }
 }
'''

CREATE_LINK_MUTATION = '''
 mutation createLinkMutation($url: String, $description: String) {
     createLink(url: $url, description: $description) {
         description
     }
 }
'''

class LinkTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.link1 = mixer.blend(Link)
        self.link2 = mixer.blend(Link)

    def test_links_query(self):
        response = self.query(
            LINKS_QUERY,
        )


        content = json.loads(response.content)
        #print(content)
        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        print ("query link results ")
        print (content)
        assert len(content['data']['links']) == 2


    def test_createLink_mutation(self):

        response = self.query(
            CREATE_LINK_MUTATION,
            variables={'url': 'https://google.com', 'description': 'google'}
        )
        print('mutation ')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual({"createLink": {"description": "google"}}, content['data']) 
