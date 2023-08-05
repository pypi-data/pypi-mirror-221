class HyperParamEntity:

    def __init__(self, x_train=None, y_train=None, x_val=None, y_val=None, alg_name=None, cv=None, model_type="",
                 scoring="", labels=None):
        if labels is None:
            labels = []
        if alg_name is None:
            alg_name = {}
        if y_val is None:
            y_val = []
        if x_val is None:
            x_val = []
        if y_train is None:
            y_train = []
        if x_train is None:
            x_train = []
        self.x_train = x_train
        self.y_train = y_train
        self.x_val = x_val
        self.y_val = y_val
        self.scoring = scoring
        self.cv = cv
        self.model_type = model_type
        self.alg_name = alg_name
        self.labels = labels


class ClasRegModelEntity:
    def __init__(self, alg, grid, model_name):
        self.alg = alg
        self.grid = grid
        self.model_name = model_name


class ModelVisualizeEntity:
    def __init__(self, alg, grid, model_name, search_type, file_name):
        self.alg = alg
        self.grid = grid
        self.model_name = model_name
        self.search_type = search_type,
        self.file_name = file_name


class MultiClasModelEntity:
    def __init__(self, alg, grid, model_name, gene_grid, gene_alg):
        self.alg = alg
        self.grid = grid
        self.model_name = model_name
        self.gene_grid = gene_grid
        self.gene_alg = gene_alg


class MultiClassGridEntity:
    def __init__(self, grid, gene_grid):
        self.grid = grid
        self.gene_grid = gene_grid


class AccuracyEntity:

    def __init__(self, file_name, score=0, val_score=0, param="", metrics="", error_msg=""):
        self.filename = file_name
        self.score = score
        self.val_score = val_score
        self.param = param
        self.metrics = metrics
        self.error_msg = error_msg


class SubmissionEntity:
    def __init__(self, predictions=None, id_=None, id_2=None, id_3=None, fields=None, file_name=None):
        if fields is None:
            fields = []
        if id_3 is None:
            id_3 = []
        if id_2 is None:
            id_2 = []
        if id_ is None:
            id_ = []
        if predictions is None:
            predictions = []
        self.predictions = predictions
        self.id_ = id_
        self.id_2 = id_2
        self.id_3 = id_3
        self.fields = fields
        self.fileName = file_name
