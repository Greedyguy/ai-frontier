<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:03:50.744696",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Infrastructure as Code",
    "CodeBERT",
    "LongFormer",
    "Static Analysis",
    "Security Misconfigurations"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Infrastructure as Code": 0.9,
    "CodeBERT": 0.85,
    "LongFormer": 0.8,
    "Static Analysis": 0.7,
    "Security Misconfigurations": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Infrastructure as Code",
        "canonical": "Infrastructure as Code",
        "aliases": [
          "IaC"
        ],
        "category": "unique_technical",
        "rationale": "A key concept in the paper, linking to discussions on automated infrastructure management.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "CodeBERT",
        "canonical": "CodeBERT",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A specific ML model used for semantic understanding in the study.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "LongFormer",
        "canonical": "LongFormer",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Another specific ML model crucial for handling long scripts in the research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Static Analysis",
        "canonical": "Static Analysis",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A foundational technique in the paper, linking to broader discussions on code analysis.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Security Misconfigurations",
        "canonical": "Security Misconfigurations",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus on detecting and mitigating security issues in IaC.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Infrastructure as Code",
      "resolved_canonical": "Infrastructure as Code",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "CodeBERT",
      "resolved_canonical": "CodeBERT",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "LongFormer",
      "resolved_canonical": "LongFormer",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Static Analysis",
      "resolved_canonical": "Static Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Security Misconfigurations",
      "resolved_canonical": "Security Misconfigurations",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# Detection of security smells in IaC scripts through semantics-aware code and language processing

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18790.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18790](https://arxiv.org/abs/2509.18790)

## 🔗 유사한 논문
- [[2025-09-24/Security smells in infrastructure as code_ a taxonomy update beyond the seven sins_20250924|Security smells in infrastructure as code: a taxonomy update beyond the seven sins]] (89.9% similar)
- [[2025-09-23/Large Language Models for Cyber Security_ A Systematic Literature Review_20250923|Large Language Models for Cyber Security: A Systematic Literature Review]] (80.2% similar)
- [[2025-09-23/Sugar-Coated Poison_ Benign Generation Unlocks LLM Jailbreaking_20250923|Sugar-Coated Poison: Benign Generation Unlocks LLM Jailbreaking]] (79.5% similar)
- [[2025-09-23/SecureFixAgent_ A Hybrid LLM Agent for Automated Python Static Vulnerability Repair_20250923|SecureFixAgent: A Hybrid LLM Agent for Automated Python Static Vulnerability Repair]] (79.5% similar)
- [[2025-09-18/Evaluating and Improving the Robustness of Security Attack Detectors Generated by LLMs_20250918|Evaluating and Improving the Robustness of Security Attack Detectors Generated by LLMs]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Static Analysis|Static Analysis]]
**⚡ Unique Technical**: [[keywords/Infrastructure as Code|Infrastructure as Code]], [[keywords/CodeBERT|CodeBERT]], [[keywords/LongFormer|LongFormer]], [[keywords/Security Misconfigurations|Security Misconfigurations]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18790v1 Announce Type: cross 
Abstract: Infrastructure as Code (IaC) automates the provisioning and management of IT infrastructure through scripts and tools, streamlining software deployment. Prior studies have shown that IaC scripts often contain recurring security misconfigurations, and several detection and mitigation approaches have been proposed. Most of these rely on static analysis, using statistical code representations or Machine Learning (ML) classifiers to distinguish insecure configurations from safe code.
  In this work, we introduce a novel approach that enhances static analysis with semantic understanding by jointly leveraging natural language and code representations. Our method builds on two complementary ML models: CodeBERT, to capture semantics across code and text, and LongFormer, to represent long IaC scripts without losing contextual information. We evaluate our approach on misconfiguration datasets from two widely used IaC tools, Ansible and Puppet. To validate its effectiveness, we conduct two ablation studies (removing code text from the natural language input and truncating scripts to reduce context) and compare against four large language models (LLMs) and prior work. Results show that semantic enrichment substantially improves detection, raising precision and recall from 0.46 and 0.79 to 0.92 and 0.88 on Ansible, and from 0.55 and 0.97 to 0.87 and 0.75 on Puppet, respectively.

## 📝 요약

이 논문은 IT 인프라를 자동화하는 코드로서의 인프라(IaC) 스크립트의 보안 오류를 탐지하기 위한 새로운 접근법을 제안합니다. 기존의 정적 분석 방법에 자연어와 코드 표현을 결합하여 의미론적 이해를 강화했습니다. CodeBERT와 LongFormer 모델을 활용하여 코드와 텍스트의 의미를 포착하고, 긴 IaC 스크립트의 문맥 정보를 유지합니다. Ansible과 Puppet의 데이터셋을 통해 평가한 결과, 제안된 방법은 탐지 성능을 크게 향상시켰으며, 정밀도와 재현율이 각각 Ansible에서 0.92와 0.88, Puppet에서 0.87과 0.75로 개선되었습니다.

## 🎯 주요 포인트

- 1. IaC(코드로서의 인프라)는 IT 인프라의 프로비저닝과 관리를 자동화하여 소프트웨어 배포를 간소화합니다.
- 2. 기존 연구에서는 IaC 스크립트에 반복적인 보안 잘못 구성 문제가 존재하며, 이를 탐지하고 완화하기 위한 여러 접근법이 제안되었습니다.
- 3. 본 연구에서는 자연어와 코드 표현을 결합하여 의미론적 이해를 강화한 새로운 정적 분석 방법을 제안합니다.
- 4. 제안된 방법은 CodeBERT와 LongFormer 모델을 사용하여 코드와 텍스트의 의미를 포착하고, 긴 IaC 스크립트를 문맥 손실 없이 표현합니다.
- 5. 연구 결과, 제안된 방법은 Ansible과 Puppet에서 보안 잘못 구성 탐지의 정밀도와 재현율을 크게 향상시켰습니다.


---

*Generated on 2025-09-24 14:03:50*