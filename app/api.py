from flask import Blueprint, jsonify
from app.models import Character

character_data = Blueprint("character_data", __name__)


@character_data.route("/characters/all", methods=["GET"])
def get_all_characters():
    try:
        characters = Character.query.all()

        character_list = []

        for character in characters:
            character_info = {
                "id": character.id,
                "name": character.name,
                "episode": character.episode,
                "chapter": character.chapter,
                "year": character.year,
                "note": character.note,
                "appearance": character.appearance,
                "personality": character.personality,
                "abilities_and_powers": character.abilities_and_powers,
            }
            character_list.append(character_info)

        return jsonify(character_list)

    except Exception as e:
        print(f"Error querying character by name: {e}")
        return None


@character_data.route("/characters/name/<name>", methods=["GET"])
def get_character_by_name(name):
    character_info = query_character_by_name(name)
    if character_info:
        return character_info
    return jsonify({"error": "Character not found"}), 404


def query_character_by_name(name):
    try:
        character = Character.query.filter_by(name=name.title()).one()
        if character:
            return jsonify(
                {
                    "id": character.id,
                    "name": character.name,
                    "episode": character.episode,
                    "chapter": character.chapter,
                    "year": character.year,
                    "note": character.note,
                    "appearance": character.appearance,
                    "personality": character.personality,
                    "abilities_and_powers": character.abilities_and_powers,
                }
            )
        return None
    except Exception as e:
        print(f"Error querying character by name: {e}")
        return None


@character_data.route("/characters/id/<id>", methods=["GET"])
def get_character_by_id(id):
    character_info = query_character_by_id(id)
    if character_info:
        return character_info
    return jsonify({"error": "Character not found"}), 404


def query_character_by_id(id):
    try:
        character = Character.query.filter_by(id=id).one()
        if character:
            return jsonify(
                {
                    "id": character.id,
                    "name": character.name,
                    "episode": character.episode,
                    "chapter": character.chapter,
                    "year": character.year,
                    "note": character.note,
                    "appearance": character.appearance,
                    "personality": character.personality,
                    "abilities_and_powers": character.abilities_and_powers,
                }
            )
        return None
    except Exception as e:
        print(f"Error querying character by name: {e}")
        return None


@character_data.route("/characters/chapter/<chapter>", methods=["GET"])
def get_character_by_chapter(chapter):
    character_info = query_character_by_chapter(chapter)
    if character_info:
        return character_info
    return jsonify({"error": "Character not found"}), 404


def query_character_by_chapter(chapter):
    try:
        full = "Chapter " + chapter
        characters = Character.query.filter_by(chapter=full).all()
        
        character_list = []

        for character in characters:
            character_info = {
                "id": character.id,
                "name": character.name,
                "episode": character.episode,
                "chapter": character.chapter,
                "year": character.year,
                "note": character.note,
                "appearance": character.appearance,
                "personality": character.personality,
                "abilities_and_powers": character.abilities_and_powers,
            }
            character_list.append(character_info)

        return jsonify(character_list)
    except Exception as e:
        print(f"Error querying character by name: {e}")
        return None


@character_data.route(
    "/characters/chapter/range/<chapter1>-<chapter2>", methods=["GET"]
)
def get_character_by_chapter_range(chapter1, chapter2):
    character_info = query_character_by_chapter_range(chapter1, chapter2)
    if character_info:
        return character_info
    return jsonify({"error": "Character not found"}), 404


def query_character_by_chapter_range(chapter1, chapter2):
    try:
        character_list = []

        for i in range(int(chapter1), int(chapter2) + 1):
            full = "Chapter " + str(i)
            characters = Character.query.filter_by(chapter=full).all()

            for character in characters:
                character_info = {
                    "id": character.id,
                    "name": character.name,
                    "episode": character.episode,
                    "chapter": character.chapter,
                    "year": character.year,
                    "note": character.note,
                    "appearance": character.appearance,
                    "personality": character.personality,
                    "abilities_and_powers": character.abilities_and_powers,
                }
                character_list.append(character_info)

        return jsonify(character_list)

    except Exception as e:
        print(f"Error querying character by name: {e}")
        return None


@character_data.route("/characters/episode/<episode>", methods=["GET"])
def get_character_by_episode(episode):
    character_info = query_character_by_episode(episode)
    if character_info:
        return character_info
    return jsonify({"error": "Character not found"}), 404


def query_character_by_episode(episode):
    try:
        full = "Episode " + episode
        characters = Character.query.filter_by(episode=full).all()
        
        character_list = []

        for character in characters:
            character_info = {
                "id": character.id,
                "name": character.name,
                "episode": character.episode,
                "chapter": character.chapter,
                "year": character.year,
                "note": character.note,
                "appearance": character.appearance,
                "personality": character.personality,
                "abilities_and_powers": character.abilities_and_powers,
            }
            character_list.append(character_info)

        return jsonify(character_list)
    except Exception as e:
        print(f"Error querying character by name: {e}")
        return None


@character_data.route(
    "/characters/episode/range/<episode1>-<episode2>", methods=["GET"]
)
def get_character_by_episode_range(episode1, episode2):
    character_info = query_character_by_episode_range(episode1, episode2)
    if character_info:
        return character_info
    return jsonify({"error": "Character not found"}), 404


def query_character_by_episode_range(episode1, episode2):
    try:
        character_list = []

        for i in range(int(episode1), int(episode2) + 1):
            full = "Episode " + str(i)
            characters = Character.query.filter_by(episode=full).all()

            for character in characters:
                character_info = {
                    "id": character.id,
                    "name": character.name,
                    "episode": character.episode,
                    "chapter": character.chapter,
                    "year": character.year,
                    "note": character.note,
                    "appearance": character.appearance,
                    "personality": character.personality,
                    "abilities_and_powers": character.abilities_and_powers,
                }
                character_list.append(character_info)

        return jsonify(character_list)

    except Exception as e:
        print(f"Error querying character by name: {e}")
        return None
    
@character_data.route("/characters/year/<year>", methods=["GET"])
def get_character_by_year(year):
    character_info = query_character_by_year(year)
    if character_info:
        return character_info
    return jsonify({"error": "Character not found"}), 404


def query_character_by_year(year):
    try:
        characters = Character.query.filter_by(year=int(year)).all()
        
        character_list = []

        for character in characters:
            character_info = {
                "id": character.id,
                "name": character.name,
                "episode": character.episode,
                "chapter": character.chapter,
                "year": character.year,
                "note": character.note,
                "appearance": character.appearance,
                "personality": character.personality,
                "abilities_and_powers": character.abilities_and_powers,
            }
            character_list.append(character_info)

        return jsonify(character_list)
    except Exception as e:
        print(f"Error querying character by name: {e}")
        return None


@character_data.route(
    "/characters/year/range/<year1>-<year2>", methods=["GET"]
)
def get_character_by_year_range(year1, year2):
    character_info = query_character_by_year_range(year1, year2)
    if character_info:
        return character_info
    return jsonify({"error": "Character not found"}), 404


def query_character_by_year_range(year1, year2):
    try:
        character_list = []

        for i in range(int(year1), int(year2) + 1):
            characters = Character.query.filter_by(year=i).all()

            for character in characters:
                character_info = {
                    "id": character.id,
                    "name": character.name,
                    "episode": character.episode,
                    "chapter": character.chapter,
                    "year": character.year,
                    "note": character.note,
                    "appearance": character.appearance,
                    "personality": character.personality,
                    "abilities_and_powers": character.abilities_and_powers,
                }
                character_list.append(character_info)

        return jsonify(character_list)

    except Exception as e:
        print(f"Error querying character by name: {e}")
        return None
    
