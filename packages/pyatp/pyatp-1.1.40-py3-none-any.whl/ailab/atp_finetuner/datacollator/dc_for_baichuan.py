from transformers import DataCollatorForSeq2Seq
from ailab.atp_finetuner.datacollator import AILabDataCollator
from ailab.atp_finetuner import constant
from ailab.atp_finetuner.preprossor import AILabPreprocessor
from ailab.atp_finetuner.build import DataCollatorRg
from ailab.atp_finetuner.constant import Task, Model

@DataCollatorRg.register((Task.question_answering, Model.baichuan_7b))
@DataCollatorRg.register((Task.question_answering, Model.baichuan_13b))
@DataCollatorRg.register((Task.question_answering, Model.bloomz_7b1_mt))
@DataCollatorRg.register((Task.question_answering, Model.falcon_7b))
@DataCollatorRg.register((Task.question_answering, Model.moss_moon_003_base))
class BaichuanDataCollator(AILabDataCollator) :
    def __init__(self, datacollator, preprocessor):
        super().__init__(datacollator, preprocessor)
    
    def forward(self, **kwargs):
        pass

    @classmethod
    def build_datacollator(cls, framework:constant.Framework, preprocessor:AILabPreprocessor) :
        tokenizer=preprocessor.preprocessor_ins
        datacollator = DataCollatorForSeq2Seq(
            tokenizer, label_pad_token_id=tokenizer.pad_token_id
        )
        return cls(datacollator, preprocessor)