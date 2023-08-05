from abc import ABC, abstractmethod
from typing import Optional, Dict, List, Any

from phi.llm.conversation.schemas import ConversationRow


class LLMStorage(ABC):
    @abstractmethod
    def create(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def read_conversation(self, conversation_id: int, user_id: str) -> Optional[ConversationRow]:
        raise NotImplementedError

    @abstractmethod
    def upsert_conversation(self, conversation: ConversationRow) -> Optional[ConversationRow]:
        raise NotImplementedError

    @abstractmethod
    def end_conversation(self, conversation_id: int, user_id: str) -> Optional[ConversationRow]:
        raise NotImplementedError

    @abstractmethod
    def delete(self) -> None:
        raise NotImplementedError

