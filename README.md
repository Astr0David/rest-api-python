# Flask Character Data API

The Flask Character Data API is a RESTful API that provides information about characters from One Piece. It offers various endpoints to query and retrieve character data based on different criteria such as name, episode, chapter, year, and more.
Find the json with list of characters in files.

### Endpoints
 - Get All Characters
   - Endpoint: /characters/all
   - Method: GET
   - Description: Get information about all characters.
 - Get Character by Name
   - Endpoint: /characters/name/<name>
   - Method: GET
   - Description: Get information about a character by name. If a character name has a space inbetween use %20
 - Get Character by ID
   - Endpoint: /characters/id/<id>
   - Method: GET
   - Description: Get information about a character by ID.
 - Get Character by Chapter
   - Endpoint: /characters/chapter/<chapter>
   - Method: GET
   - Description: Get information about characters introduced from specific chapter.
 - Get Characters by Chapter Range
   - Endpoint: /characters/chapter/range/<chapter1>-<chapter2>
   - Method: GET
   - Description: Get information about characters introduced from a range of chapters.
 - Get Character by Episode
   - Endpoint: /characters/episode/<episode>
   - Method: GET
   - Description: Get information about characters introduced from a specific episode.
 - Get Characters by Episode Range
   - Endpoint: /characters/episode/range/<episode1>-<episode2>
   - Method: GET
   - Description: Get information about characters introduced from a range of episodes.
 - Get Character by Year
   - Endpoint: /characters/year/<year>
   - Method: GET
   - Description: Get information about characters introduced in a specific year.
 - Get Characters by Year Range
   - Endpoint: /characters/year/range/<year1>-<year2>
   - Method: GET
   - Description: Get information about characters introduced in a range of years.
