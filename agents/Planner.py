from llm.llm import LLM

class Planner:
    f1_api_schema = {
    "car_data": [
        "brake", "date", "driver_number", "drs", "meeting_key", 
        "n_gear", "rpm", "session_key", "speed", "throttle"
    ],
    "championship_drivers": [
        "driver_number", "meeting_key", "points_current", "points_start", 
        "position_current", "position_start", "session_key"
    ],
    "championship_teams": [
        "meeting_key", "points_current", "points_start", "position_current", 
        "position_start", "session_key", "team_name"
    ],
    "drivers": [
        "broadcast_name", "driver_number", "first_name", "full_name", 
        "last_name", "meeting_key", "name_acronym", "session_key", 
        "team_colour", "team_name"
    ],
    "intervals": [
        "date", "driver_number", "gap_to_leader", "interval", 
        "meeting_key", "session_key"
    ],
    "laps": [
        "date_start", "driver_number", "duration_sector_1", "duration_sector_2", 
        "duration_sector_3", "i1_speed", "i2_speed", "is_pit_out_lap", 
        "lap_duration", "lap_number", "meeting_key", "segments_sector_1", 
        "segments_sector_2", "segments_sector_3", "session_key", "st_speed"
    ],
    "location": [
        "date", "driver_number", "meeting_key", "session_key", "x", "y", "z"
    ],
    "meetings": [
        "circuit_key", "circuit_short_name", "circuit_type", "country_code", 
        "country_key", "country_name", "date_end", "date_start", "gmt_offset", 
        "location", "meeting_key", "meeting_name", "meeting_official_name", "year"
    ],
    "overtakes": [
        "date", "meeting_key", "overtaken_driver_number", 
        "overtaking_driver_number", "position", "session_key"
    ],
    "position": [
        "date", "driver_number", "meeting_key", "position", "session_key"
    ],
    "sessions": [
        "circuit_key", "circuit_short_name", "country_code", "country_key", 
        "country_name", "date_end", "date_start", "gmt_offset", "location", 
        "meeting_key", "session_key", "session_name", "session_type", "year"
    ],
    "session_result": [
        "dnf", "dns", "dsq", "driver_number", "duration", "gap_to_leader", 
        "number_of_laps", "meeting_key", "position", "session_key"
    ]
}

    
    prompt = f"Analyse the the query and strictly give me a Python comma seperated list of working urls for fetchiing data from OpenF1 API, and the urls should be in the format of https://api.openf1.org/v1/{"endpoint"}?{"parameter"} where endpoints and the parameters are given in {f1_api_schema}. As needed for a particular endpoint, multiple parameters can be given in the url and the parameters should be in the format of {"parameter"}={"value"}. There should no other responce other then a python List and if the query is not related to F1 or if the query is too general and cannot be answered with the given endpoints, then respond with an empty list."
    
    def planner(self, query):
        llm = LLM()
        contents= f"This is the query: {query}. {self.prompt}"
        response = llm.generate_content(contents)
        urls = response.split(",") if response else []
        urls = [url.strip() for url in urls]
        return urls
    