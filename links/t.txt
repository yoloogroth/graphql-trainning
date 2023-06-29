from django.test import TestCase

# Create your tests here.
from links.schema import Query
from links.schema import Mutation
import graphene

class LinkTest(TestCase):
    fixtures = ["fixture1.json"]

    def setUp(self):
        super().setUp()

        self.queryLink = """
            query {
              links {
                id
              }
            }
        """
        self.mutationLink = """
            mutation {
              createLink(description:"google", url:"google") {
                description
              }
            }
        """
    def testMutationLink(self):
        schema = graphene.Schema(mutation=Mutation)
        result = schema.execute(self.mutationLink)
        self.assertIsNone(result.errors)
        print ("mutation link results ")
        print (result.data)

        self.assertDictEqual({"createLink": {"description": "google"}}, result.data)


    def testQueryLink(self):
        schema = graphene.Schema(query=Query)
        result = schema.execute(self.queryLink)
        self.assertIsNone(result.errors)
        print ("query link results ")
        print (result.data)
        self.assertDictEqual({"links": [{'id': '1'}] }, result.data)


#import json
#from graphene_django.utils.testing import GraphQLTestCase

#class MyFancyTestCase(GraphQLTestCase):
#    def test_some_query(self):
#        response = self.query(
#            '''
#            query {
#                links {
#                    id
#                }
#            }
#            ''',
#            op_name='links'
#        )


#content = json.loads(response.content.data)

        # This validates the status code and if you get errors
 #       self.assertResponseNoErrors(response)
