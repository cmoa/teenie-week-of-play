This experiemental tool can extract information from and refine Library of Congress Subject Headers. 

We use the exisiting subject headings to take an educated guess at the photographed location, searching the key points and place qualifiers with Google’s Geocoding API. 

We check the Library of Congress and other sources to suggest better ways to format existing subject headers. Included in the result is the Library of Congress link to the suggested subject, where you can find a list of related terms. 

To get started:
- Download this repository.
- In terminal, `cd teenie-week-of-play/SubjectHeaders/`
- In terminal, `python -m SimpleHTTPServer`
- In a browser, visit `http://localhost:8000/teenie.html`

