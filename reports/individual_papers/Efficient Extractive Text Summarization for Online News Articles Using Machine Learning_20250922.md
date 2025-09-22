# Efficient Extractive Text Summarization for Online News Articles Using Machine Learning

**Korean Title:** 온라인 뉴스 기사에 대한 효율적인 추출적 텍스트 요약을 위한 기계 학습 사용

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: BERT Embeddings, Long Short-Term Memory Networks

## 🔗 유사한 논문
- [[2025-09-22/Re-FRAME the Meeting Summarization SCOPE_ Fact-Based Summarization and Personalization via Questions_20250922|Re-FRAME the Meeting Summarization SCOPE Fact-Based Summarization and Personalization via Questions]] (81.1% similar)
- [[2025-09-22/Deep learning and abstractive summarisation for radiological reports_ an empirical study for adapting the PEGASUS models' family with scarce data_20250922|Deep learning and abstractive summarisation for radiological reports an empirical study for adapting the PEGASUS models' family with scarce data]] (80.7% similar)
- [[2025-09-19/MOLE_ Metadata Extraction and Validation in Scientific Papers Using LLMs_20250919|MOLE Metadata Extraction and Validation in Scientific Papers Using LLMs]] (80.4% similar)
- [[2025-09-22/CORE-RAG_ Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning_20250922|CORE-RAG Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning]] (79.9% similar)
- [[2025-09-19/When Content is Goliath and Algorithm is David_ The Style and Semantic Effects of Generative Search Engine_20250919|When Content is Goliath and Algorithm is David The Style and Semantic Effects of Generative Search Engine]] (79.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15614v1 Announce Type: new 
Abstract: In the age of information overload, content management for online news articles relies on efficient summarization to enhance accessibility and user engagement. This article addresses the challenge of extractive text summarization by employing advanced machine learning techniques to generate concise and coherent summaries while preserving the original meaning. Using the Cornell Newsroom dataset, comprising 1.3 million article-summary pairs, we developed a pipeline leveraging BERT embeddings to transform textual data into numerical representations. By framing the task as a binary classification problem, we explored various models, including logistic regression, feed-forward neural networks, and long short-term memory (LSTM) networks. Our findings demonstrate that LSTM networks, with their ability to capture sequential dependencies, outperform baseline methods like Lede-3 and simpler models in F1 score and ROUGE-1 metrics. This study underscores the potential of automated summarization in improving content management systems for online news platforms, enabling more efficient content organization and enhanced user experiences.

## 🔍 Abstract (한글 번역)

arXiv:2509.15614v1 발표 유형: 신규  
초록: 정보 과부하 시대에 온라인 뉴스 기사의 콘텐츠 관리는 접근성과 사용자 참여를 향상시키기 위해 효율적인 요약에 의존합니다. 이 논문은 원래의 의미를 보존하면서 간결하고 일관된 요약을 생성하기 위해 고급 기계 학습 기술을 활용하여 추출적 텍스트 요약의 도전을 다룹니다. 130만 개의 기사-요약 쌍으로 구성된 Cornell Newsroom 데이터셋을 사용하여, 우리는 BERT 임베딩을 활용하여 텍스트 데이터를 수치적 표현으로 변환하는 파이프라인을 개발했습니다. 이 작업을 이진 분류 문제로 설정하여, 로지스틱 회귀, 피드포워드 신경망, 장단기 메모리 (LSTM) 네트워크를 포함한 다양한 모델을 탐구했습니다. 우리의 연구 결과는 순차적 의존성을 포착하는 능력을 가진 LSTM 네트워크가 Lede-3와 같은 기본 방법 및 더 간단한 모델보다 F1 점수와 ROUGE-1 지표에서 우수하다는 것을 보여줍니다. 이 연구는 온라인 뉴스 플랫폼의 콘텐츠 관리 시스템을 개선하여 더 효율적인 콘텐츠 조직과 향상된 사용자 경험을 가능하게 하는 자동 요약의 잠재력을 강조합니다.

## 📝 요약

이 논문은 정보 과부하 시대에 온라인 뉴스 기사의 효율적인 요약을 통해 접근성과 사용자 참여를 높이는 방법을 제시합니다. Cornell Newsroom 데이터셋을 활용하여 BERT 임베딩을 통해 텍스트 데이터를 수치화하고, 이를 이진 분류 문제로 설정하여 다양한 모델을 탐구했습니다. 그 결과, 순차적 의존성을 포착하는 LSTM 네트워크가 Lede-3 등의 기준 방법보다 F1 점수와 ROUGE-1 지표에서 우수한 성능을 보였습니다. 이 연구는 자동 요약의 잠재력을 강조하며, 온라인 뉴스 플랫폼의 콘텐츠 관리 시스템 개선에 기여할 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. 정보 과부하 시대에 온라인 뉴스 기사의 효율적인 요약은 접근성과 사용자 참여를 높이는 데 중요하다.

- 2. 본 연구는 고급 기계 학습 기법을 활용하여 원래 의미를 유지하면서 간결하고 일관된 요약을 생성하는 방법을 제시한다.

- 3. Cornell Newsroom 데이터셋을 사용하여 BERT 임베딩을 통해 텍스트 데이터를 수치화하고, 이를 이진 분류 문제로 접근하였다.

- 4. LSTM 네트워크가 순차적 의존성을 포착하는 능력 덕분에 Lede-3 및 단순 모델보다 F1 점수와 ROUGE-1 지표에서 우수한 성능을 보였다.

- 5. 자동 요약의 잠재력은 온라인 뉴스 플랫폼의 콘텐츠 관리 시스템을 개선하고 사용자 경험을 향상시키는 데 기여할 수 있다.

---

*Generated on 2025-09-22 15:21:09*