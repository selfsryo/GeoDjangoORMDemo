import shutil
from pathlib import Path

from django.contrib.gis.utils import LayerMapping
from world.models import AdminiBoundary, Airport

airport_mapping = {
    "c28_001": "C28_001",
    "c28_003": "C28_003",
    "c28_004": "C28_004",
    "c28_005": "C28_005",
    "c28_006": "C28_006",
    "c28_007": "C28_007",
    "c28_008": "C28_008",
    "c28_009": "C28_009",
    "c28_010": "C28_010",
    "c28_011": "C28_011",
    "c28_012": "C28_012",
    "c28_013": "C28_013",
    "c28_101": "C28_101",
    "c28_102": "C28_102",
    "c28_103": "C28_103",
    "c28_104": "C28_104",
    "c28_000": "C28_000",
    "geom": "MULTIPOLYGON",
}
adminiboundary_mapping = {
    "n03_001": "N03_001",
    "n03_002": "N03_002",
    "n03_003": "N03_003",
    "n03_004": "N03_004",
    "n03_007": "N03_007",
    "geom": "MULTIPOLYGON",
}


airport_zip = Path(__file__).resolve().parent / "data/C28-21_GML.zip"
airport_shp = Path(__file__).resolve().parent / "data/C28-21_GML/C28-21_Airport.shp"

adminiboundary_zip = Path(__file__).resolve().parent / "data/N03-20220101_01_GML.zip"
adminiboundary_shp = Path(__file__).resolve().parent / "data/N03-20220101_01_GML/N03-22_01_220101.shp"


class LoadData:
    """zipを解凍して対象のshpをDB読み込み"""

    def __init__(self, zip_path, shp_path, mapping, model):
        self.zip_path = zip_path
        self.shp_path = shp_path
        self.mapping = mapping
        self.model = model

    def unzip(self):
        shutil.unpack_archive(self.zip_path, self.shp_path.parent)

    def load(self, verbose=True):
        lm = LayerMapping(self.model, self.shp_path, self.mapping, transform=False)
        lm.save(strict=True, verbose=verbose)

    def run(self):
        if not Path(self.shp_path.parent).exists():
            self.unzip()
        self.load()


def main():
    LoadData(airport_zip, airport_shp, airport_mapping, Airport).run()
    LoadData(adminiboundary_zip, adminiboundary_shp, adminiboundary_mapping, AdminiBoundary).run()
