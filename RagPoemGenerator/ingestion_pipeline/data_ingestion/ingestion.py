from importlib import metadata
from typing import List
from dataclasses import dataclass,asdict
import json

from sympy import content
from tomlkit import document

@dataclass
class Document:
    content:str
    metadata:dict

class IngestionPipeline:
    @staticmethod
    def load_file(file_path:str)->str:
        with open(file_path,"r",encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def chunk_text(text:strt)->List[str]:
        chunks=text.split("\n## ")
        result=[]
        for chunk in chunks:
            chunk=chunk.strip()
            if chunk:
                result.append(chunk)
        return result

    @staticmethod
    def create_documents(chunks:List[str])->List[Document]:
        documents=[]
        for chunk in chunks:
            lines=[line.strip() for line in chunk.split("\n") if line.strip()]
            if len(lines)<4:
                continue
            date=lines[0]
            location=lines[1].replace("### Location:", "").strip()
            mood=lines[-1].replace("Mood:","").strip()
            content=(
                f"Date: {date}\n"
                f"Location: {location}\n\n"
                +"\n".join(lines[2:-1])
            )

            document=Document(
                content=content,
                metadata={
                    "date": date,
                    "location": location,
                    "mood": mood
                }
            )

            documents.append(document)
        return documents

    def run_pipeline(self,file_path:str)->List[Document]:
        texts=self.load_file(file_path)
        chunks=self.chunk_text(texts)
        documents=self.create_documents(chunks)
        return documents

    @staticmethod
    def save_documents(documents:List[Document],output_path:str)->None:
        with open(output_path,"w",encoding="utf-8") as f:
            json.dump(
                [asdict(doc) for doc in documents],
                f,
                indent=4,
                ensure_ascii=False
            )

# if __name__=="__main__":
    