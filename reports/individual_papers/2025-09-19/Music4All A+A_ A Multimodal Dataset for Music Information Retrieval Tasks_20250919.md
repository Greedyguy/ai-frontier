
# Music4All A+A: A Multimodal Dataset for Music Information Retrieval Tasks

**Korean Title:** 음악 정보 검색 작업을 위한 다중 모달 데이터셋: Music4All A+A

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multimodal Music Recommendation

## 🔗 유사한 논문
- [[Two Web Toolkits for Multimodal Piano Performance Dataset Acquisition and Fingering Annotation_20250919|Two Web Toolkits for Multimodal Piano Performance Dataset Acquisition and Fingering Annotation]] (79.7% similar)
- [[MOLE Metadata Extraction and Validation in Scientific Papers Using LLMs]] (77.5% similar)
- [[UnifiedVisual A Framework for Constructing Unified Vision-Language Datasets]] (76.7% similar)
- [[Omni-CLST Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering]] (76.7% similar)
- [[MARS2 2025 Challenge on Multimodal Reasoning Datasets, Methods, Results, Discussion, and Outlook]] (76.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14891v1 Announce Type: cross 
Abstract: Music is characterized by aspects related to different modalities, such as the audio signal, the lyrics, or the music video clips. This has motivated the development of multimodal datasets and methods for Music Information Retrieval (MIR) tasks such as genre classification or autotagging. Music can be described at different levels of granularity, for instance defining genres at the level of artists or music albums. However, most datasets for multimodal MIR neglect this aspect and provide data at the level of individual music tracks. We aim to fill this gap by providing Music4All Artist and Album (Music4All A+A), a dataset for multimodal MIR tasks based on music artists and albums. Music4All A+A is built on top of the Music4All-Onion dataset, an existing track-level dataset for MIR tasks. Music4All A+A provides metadata, genre labels, image representations, and textual descriptors for 6,741 artists and 19,511 albums. Furthermore, since Music4All A+A is built on top of Music4All-Onion, it allows access to other multimodal data at the track level, including user--item interaction data. This renders Music4All A+A suitable for a broad range of MIR tasks, including multimodal music recommendation, at several levels of granularity. To showcase the use of Music4All A+A, we carry out experiments on multimodal genre classification of artists and albums, including an analysis in missing-modality scenarios, and a quantitative comparison with genre classification in the movie domain. Our experiments show that images are more informative for classifying the genres of artists and albums, and that several multimodal models for genre classification struggle in generalizing across domains. We provide the code to reproduce our experiments at https://github.com/hcai-mms/Music4All-A-A, the dataset is linked in the repository and provided open-source under a CC BY-NC-SA 4.0 license.

## 🔍 Abstract (한글 번역)

arXiv:2509.14891v1 발표 유형: 교차  
초록: 음악은 오디오 신호, 가사, 뮤직 비디오 클립과 같은 다양한 양식과 관련된 측면에 의해 특징지어집니다. 이는 장르 분류나 자동 태깅과 같은 음악 정보 검색(MIR) 작업을 위한 다중 양식 데이터셋과 방법의 개발을 촉진했습니다. 음악은 예술가나 음악 앨범 수준에서 장르를 정의하는 등 다양한 세분화 수준에서 설명될 수 있습니다. 그러나 다중 양식 MIR을 위한 대부분의 데이터셋은 이 측면을 무시하고 개별 음악 트랙 수준의 데이터를 제공합니다. 우리는 음악 아티스트와 앨범을 기반으로 한 다중 양식 MIR 작업을 위한 데이터셋인 Music4All Artist and Album (Music4All A+A)을 제공하여 이 격차를 메우고자 합니다. Music4All A+A는 MIR 작업을 위한 기존 트랙 수준 데이터셋인 Music4All-Onion을 기반으로 구축되었습니다. Music4All A+A는 6,741명의 아티스트와 19,511개의 앨범에 대한 메타데이터, 장르 레이블, 이미지 표현 및 텍스트 설명자를 제공합니다. 더욱이, Music4All A+A는 Music4All-Onion을 기반으로 구축되었기 때문에 사용자-항목 상호작용 데이터 등 트랙 수준의 다른 다중 양식 데이터에 접근할 수 있습니다. 이는 Music4All A+A를 여러 세분화 수준에서 다중 양식 음악 추천을 포함한 다양한 MIR 작업에 적합하게 만듭니다. Music4All A+A의 사용을 보여주기 위해, 우리는 아티스트와 앨범의 다중 양식 장르 분류에 대한 실험을 수행했으며, 누락된 양식 시나리오에 대한 분석과 영화 도메인에서의 장르 분류와의 정량적 비교를 포함했습니다. 우리의 실험은 이미지가 아티스트와 앨범의 장르를 분류하는 데 더 많은 정보를 제공하며, 여러 다중 양식 장르 분류 모델이 도메인 간 일반화에 어려움을 겪고 있음을 보여줍니다. 우리의 실험을 재현하기 위한 코드는 https://github.com/hcai-mms/Music4All-A-A에서 제공되며, 데이터셋은 저장소에 연결되어 있으며 CC BY-NC-SA 4.0 라이선스 하에 오픈 소스로 제공됩니다.

## 📝 요약

이 논문은 음악 정보 검색(MIR) 작업을 위한 다중 모달 데이터셋인 Music4All Artist and Album (Music4All A+A)을 소개합니다. 기존의 트랙 수준 데이터셋인 Music4All-Onion을 기반으로 하여 아티스트와 앨범 수준에서 메타데이터, 장르 레이블, 이미지, 텍스트 설명을 제공합니다. 이를 통해 다양한 수준의 MIR 작업, 특히 다중 모달 음악 추천에 적합합니다. 실험 결과, 이미지가 아티스트와 앨범의 장르 분류에 유용하며, 여러 다중 모달 모델이 도메인 간 일반화에 어려움을 겪는다는 것을 보여줍니다. 실험 재현을 위한 코드는 GitHub에 공개되어 있습니다.

## 🎯 주요 포인트

- 1. Music4All Artist and Album (Music4All A+A) 데이터셋은 음악 아티스트와 앨범을 기반으로 한 다중 모달 음악 정보 검색(MIR) 작업을 지원합니다.

- 2. Music4All A+A는 Music4All-Onion 데이터셋을 기반으로 구축되어, 트랙 수준의 다중 모달 데이터 및 사용자-아이템 상호작용 데이터를 제공합니다.

- 3. 이 데이터셋은 6,741명의 아티스트와 19,511개의 앨범에 대한 메타데이터, 장르 레이블, 이미지 표현 및 텍스트 설명을 포함합니다.

- 4. 실험 결과, 이미지가 아티스트와 앨범의 장르 분류에 있어 더 많은 정보를 제공하며, 여러 다중 모달 모델들이 도메인 간 일반화에 어려움을 겪는 것으로 나타났습니다.

- 5. 연구팀은 실험 재현을 위한 코드를 제공하며, 데이터셋은 CC BY-NC-SA 4.0 라이선스 하에 오픈 소스로 제공됩니다.

---

*Generated on 2025-09-19 16:25:42*