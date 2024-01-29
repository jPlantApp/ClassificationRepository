from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Functions.db import Flower
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

uname = config.get('database', 'uname')
passwd = config.get('database', 'passwd')
host = config.get('database', 'host')
dbname = config.get('database', 'dbname')

engine = create_engine(f'postgresql://{uname}:{passwd}@{host}/{dbname}')
Session = sessionmaker(bind=engine)
session = Session()

flower_data = [
    {"name": "Adenium Obesum", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Alstroemeria", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Amaryllis", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Anemone", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Aquilegia alpina", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Astrantia", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Azalea", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Black Cumin", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Blackberry Lilly", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Blue Eryngo", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Blue Hibiscus", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Bold Look Iris", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Bougainvillea", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Bull Thistle", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Calendula Officinalis", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "California Poppy", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Calla Lilly", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Campanula Blue", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Campsis Radicans", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Canna Lilly", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Carduus Cardunculus", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Carnation", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Cautleya", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Clematis Florida", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Coltsfoot", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Crimson Catteleya", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Crocus", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Cyclamen", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Daffodil", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Dalia Bishop od Llandaff", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Dalia Melody", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Dandelions", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Datura Bernhardii", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Dianthus", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Echinops", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Erysimum", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Frangipani", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Fritillaria", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Garden Cosmos", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Garden Phlox", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Gazania", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Gentiana Acaulis", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Geranium", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Gerbera", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Gladiolus", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Globeflower", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Gloriosa", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Grape Hyacinth", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Guzmania", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Heartsease", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Helleborus", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Indian Blanket", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Japanese Camellia", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Japanese Thimbleweed", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "King Protea", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Laceleaf", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Ladys Glove", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Lotus", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Magnolia Sprengeri", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Marguerite Daisy", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Marigold", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Matilija Poppy", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Meadow Buttercup", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Mexican Sunflower", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Monkshood", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Morning Glory", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Nerine", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Nymphaea Tetragona", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Osteospermum", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Paphiopedilum Micranthum", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Passiflora Caerulea", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Pea Prince", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Petunia", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Phalaenopsis Aphrodite", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Pink Quill", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Pinkladies", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Platycodon", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Poinsettia", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Poppy", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Primula", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Purple Coneflower", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Red Ginger", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Rose", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Rudbeckia", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Ruellia Tuberosa", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Scarlet Beebalm", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Shoeblackplant", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Siam Tulip", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Silverbush", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Snapdragon", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Strelitzia", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Sunflower", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Surfinia", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Sweet Scabious", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Texas Bluebell", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Tiger Lilly", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Tricyrtis", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Tropaeolum Majus", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "White Gaura", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None},
    {"name": "Yellow Iris", "description": None, "growing": None, "usage": None, "flowering": None, "winterizing": None, "notes": None}
]

flowers = [Flower(**data) for data in flower_data]
session.add_all(flowers)
session.commit()