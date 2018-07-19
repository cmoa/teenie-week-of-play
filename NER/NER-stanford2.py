import corenlp

text = "Chris wrote a simple sentence that he parsed with Stanford CoreNLP."

# We assume that you've downloaded Stanford CoreNLP and defined an environment
# variable $CORENLP_HOME that points to the unzipped directory.
# The code below will launch StanfordCoreNLPServer in the background
# and communicate with the server to annotate the sentence.
with corenlp.CoreNLPClient(annotators="tokenize ssplit".split()) as client:
  ann = client.annotate(text)
