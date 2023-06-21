from typing import List

from langchain.schema import Document

from pilot import SourceEmbedding, register


class StringEmbedding(SourceEmbedding):
    """
    string embedding for read string document.
    """

    def __init__(self, file_path, vector_store_config):
        """
        Initialize with pdf path.
        """
        # [
        #       '{"table_name": "adwetec_aihub_car_configuration_basic", "table_description": "新能源汽车基本信息表"}',
        #       '{"table_name": "adwetec_aihub_car_configuration_body", "table_description": "新能源汽车车身相关信息表"}',
        #       '{"table_name": "adwetec_aihub_car_configuration_gearbox", "table_description": ""}',
        #       '{"table_name": "adwetec_aihub_car_configuration_motor", "table_description": "新能源汽车动力信息表"}'
        # ]
        # {
        #       'vector_store_name': 'adwetec_aihub_cars_summary',
        #       'embeddings': HuggingFaceEmbeddings(
        #           client=SentenceTransformer(
        #               (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel
        #               (1): Pooling({
        #                   'word_embedding_dimension': 1024,
        #                   'pooling_mode_cls_token': False,
        #                   'pooling_mode_mean_tokens': True,
        #                   'pooling_mode_max_tokens': False,
        #                   'pooling_mode_mean_sqrt_len_tokens': False
        #               })
        #           ),
        #           model_name='F:\\workspace\\github\\xiedongmingming\\DB-GPT\\models\\text2vec-large-chinese'
        #       )
        # }
        super().__init__(file_path, vector_store_config)

        self.file_path = file_path

        self.vector_store_config = vector_store_config

    @register
    def read(self):
        """
        Load from String path.
        """
        metadata = {"source": "db_summary"}

        return [Document(page_content=self.file_path, metadata=metadata)]

    @register
    def data_process(self, documents: List[Document]):
        #
        i = 0

        for d in documents:
            #
            documents[i].page_content = d.page_content.replace("\n", "")

            i += 1

        return documents
