from configuration_bert import BertConfig
from tokenization_bert import BertTokenizer
from modeling_bert import BertEncoder


bert_config = BertConfig()
bert_encoder = BertEncoder(bert_config)

