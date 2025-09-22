
# TFLAG:Towards Practical APT Detection via Deviation-Aware Learning on Temporal Provenance Graph

**Korean Title:** TFLAG: 시간적 근원 그래프에서의 이탈 감지 학습을 통한 실용적 APT 탐지 방향

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Temporal Provenance Graph

## 🔗 유사한 논문
- [[Learning Temporal Invariance in Android Malware Detectors]] (79.9% similar)
- [[BERTector_An_Intrusion_Detection_Framework_Constructed_via_Joint-dataset_Learning_Based_on_Language_Model_20250918|BERTector: An Intrusion Detection Framework Constructed via Joint-dataset Learning Based on Language Model]] (79.3% similar)
- [[Anomaly_Detection_in_Offshore_Open_Radio_Access_Network_Using_Long_Short-Term_Memory_Models_on_a_Novel_Artificial_Intelligence-Driven_Cloud-Native_Data_Platform_20250918|Anomaly Detection in Offshore Open Radio Access Network Using Long Short-Term Memory Models on a Novel Artificial Intelligence-Driven Cloud-Native Data Platform]] (77.6% similar)
- [[DiffHash_Text-Guided_Targeted_Attack_via_Diffusion_Models_against_Deep_Hashing_Image_Retrieval_20250918|DiffHash: Text-Guided Targeted Attack via Diffusion Models against Deep Hashing Image Retrieval]] (77.0% similar)
- [[Search-TTA: A Multimodal Test-Time Adaptation Framework for Visual Search in the Wild]] (76.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.06997v2 Announce Type: replace 
Abstract: Advanced Persistent Threat (APT) have grown increasingly complex and concealed, posing formidable challenges to existing Intrusion Detection Systems in identifying and mitigating these attacks. Recent studies have incorporated graph learning techniques to extract detailed information from provenance graphs, enabling the detection of attacks with greater granularity. Nevertheless, existing studies have largely overlooked the continuous yet subtle temporal variations in the structure of provenance graphs, which may correspond to surreptitious perturbation anomalies in ongoing APT attacks. Therefore, we introduce TFLAG, an advanced anomaly detection framework that for the first time integrates the structural dynamic extraction capabilities of temporal graph model with the anomaly delineation abilities of deviation networks to pinpoint covert attack activities in provenance graphs. This self-supervised integration framework leverages the graph model to extract neighbor interaction data under continuous temporal changes from historical benign behaviors within provenance graphs, while simultaneously utilizing deviation networks to accurately distinguish authentic attack activities from false positive deviations due to unexpected subtle perturbations. The experimental results indicate that, through a comprehensive design that utilizes both attribute and temporal information, it can accurately identify the time windows associated with APT attack behaviors without prior knowledge (e.g., labeled data samples), demonstrating superior accuracy compared to current state-of-the-art methods in differentiating between attack events and system false positive events.

## 🔍 Abstract (한글 번역)

arXiv:2501.06997v2 발표 유형: 대체
요약: 고도로 지속되는 위협(Advanced Persistent Threat, APT)은 점점 복잡하고 숨겨져 있어 기존 침입 탐지 시스템이 이러한 공격을 식별하고 완화하는 데 엄청난 어려움을 겪고 있습니다. 최근 연구에서는 출처 그래프로부터 상세한 정보를 추출하기 위해 그래프 학습 기술을 통합하여, 공격을 더 세밀하게 감지할 수 있게 되었습니다. 그러나 기존 연구는 출처 그래프의 지속적이고 섬세한 시간적 변화를 대부분 간과했는데, 이는 진행 중인 APT 공격의 은밀한 변형 이상 현상에 해당할 수 있습니다. 따라서 우리는 TFLAG를 소개합니다. 이는 출처 그래프에서 은밀한 공격 활동을 정확히 지목하기 위해 시간적 그래프 모델의 구조적 동적 추출 능력과 이상 현상 구분 능력을 통합한 첨단 이상 감지 프레임워크입니다. 이 자가 감독 통합 프레임워크는 출처 그래프 내에서 과거의 양호한 행동으로부터 연속적인 시간적 변화 속에서 이웃 상호 작용 데이터를 추출하기 위해 그래프 모델을 활용하면서, 동시에 예상치 못한 섬세한 변동으로 인한 잘못된 양성 이상 현상과 진정한 공격 활동을 정확하게 구분하기 위해 이상 현상 네트워크를 활용합니다. 실험 결과는 속성 및 시간 정보를 모두 활용한 종합적 설계를 통해, 라벨링된 데이터 샘플과 같은 사전 지식 없이도 APT 공격 행동과 시스템의 잘못된 양성 이벤트를 구분하는 데 현재 최첨단 기법보다 우수한 정확도를 보여준다는 것을 나타냅니다.

## 📝 요약

최근 연구들은 그래프 학습 기술을 도입하여 원천 그래프로부터 상세한 정보를 추출하여 APT 공격을 더 세밀하게 탐지할 수 있게 되었다. 그러나 기존 연구들은 원천 그래프의 연속적이고 섬세한 시간적 변화를 간과해왔다. 이에 우리는 TFLAG를 소개하며, 시간 그래프 모델의 구조적 동적 추출 기능과 이탈 네트워크의 이상 탐지 능력을 통합하여 원천 그래프에서 은밀한 공격 활동을 정확히 식별하는 고급 이상 탐지 프레임워크를 처음으로 제안한다. 실험 결과는 속성 및 시간 정보를 모두 활용한 종합적 설계를 통해 라벨링된 데이터 샘플과 같은 사전 지식 없이 APT 공격 행위와 시스템 잘못된 양성 이벤트를 구별하는 데 우수한 정확도를 보여줌을 나타낸다.

## 🎯 주요 포인트

- 1. APT는 점점 복잡하고 숨겨져 있어서 기존 침입 탐지 시스템에 엄청난 도전을 제공하고 있음.

- 2. TFLAG는 구조적 동적 추출 능력과 이상 탐지 능력을 통합하여 증거 그래프에서 은밀한 공격 활동을 정확히 식별함.

- 3. 실험 결과는 TFLAG가 APT 공격 행위를 정확히 식별하는 데 우수한 정확도를 보여줌.

---

*Generated on 2025-09-18 17:11:06*