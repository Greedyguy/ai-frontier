<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:02:08.658649",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Infrastructure as Code",
    "Security Smells",
    "DevSecOps",
    "Terraform",
    "Large Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Infrastructure as Code": 0.78,
    "Security Smells": 0.85,
    "DevSecOps": 0.81,
    "Terraform": 0.79,
    "Large Language Model": 0.8
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
        "category": "broad_technical",
        "rationale": "A foundational concept in the paper, essential for understanding the context of security smells.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "security smells",
        "canonical": "Security Smells",
        "aliases": [
          "code smells",
          "security vulnerabilities"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's contribution, offering a taxonomy that can be linked to security practices.",
        "novelty_score": 0.72,
        "connectivity_score": 0.79,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "DevSecOps practices",
        "canonical": "DevSecOps",
        "aliases": [
          "Development Security Operations"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the integration of security into DevOps, a key practice for addressing security smells.",
        "novelty_score": 0.58,
        "connectivity_score": 0.83,
        "specificity_score": 0.76,
        "link_intent_score": 0.81
      },
      {
        "surface": "Terraform",
        "canonical": "Terraform",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "One of the popular IaC tools analyzed, relevant for linking tool-specific security insights.",
        "novelty_score": 0.55,
        "connectivity_score": 0.84,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Used in the paper for automation, linking to broader AI and NLP discussions.",
        "novelty_score": 0.5,
        "connectivity_score": 0.87,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "Cloud Web Services",
      "GitHub projects"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Infrastructure as Code",
      "resolved_canonical": "Infrastructure as Code",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "security smells",
      "resolved_canonical": "Security Smells",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.79,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "DevSecOps practices",
      "resolved_canonical": "DevSecOps",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.83,
        "specificity": 0.76,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Terraform",
      "resolved_canonical": "Terraform",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.84,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.87,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Security smells in infrastructure as code: a taxonomy update beyond the seven sins

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18761.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18761](https://arxiv.org/abs/2509.18761)

## 🔗 유사한 논문
- [[2025-09-23/SecureFixAgent_ A Hybrid LLM Agent for Automated Python Static Vulnerability Repair_20250923|SecureFixAgent: A Hybrid LLM Agent for Automated Python Static Vulnerability Repair]] (80.7% similar)
- [[2025-09-22/SeCodePLT_ A Unified Platform for Evaluating the Security of Code GenAI_20250922|SeCodePLT: A Unified Platform for Evaluating the Security of Code GenAI]] (80.6% similar)
- [[2025-09-17/A Taxonomy of Prompt Defects in LLM Systems_20250917|A Taxonomy of Prompt Defects in LLM Systems]] (79.5% similar)
- [[2025-09-19/Exploit Tool Invocation Prompt for Tool Behavior Hijacking in LLM-Based Agentic System_20250919|Exploit Tool Invocation Prompt for Tool Behavior Hijacking in LLM-Based Agentic System]] (78.9% similar)
- [[2025-09-23/Large Language Models for Cyber Security_ A Systematic Literature Review_20250923|Large Language Models for Cyber Security: A Systematic Literature Review]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Infrastructure as Code|Infrastructure as Code]], [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/DevSecOps|DevSecOps]], [[keywords/Terraform|Terraform]]
**⚡ Unique Technical**: [[keywords/Security Smells|Security Smells]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18761v1 Announce Type: cross 
Abstract: Infrastructure as Code (IaC) has become essential for modern software management, yet security flaws in IaC scripts can have severe consequences, as exemplified by the recurring exploits of Cloud Web Services. Prior work has recognized the need to build a precise taxonomy of security smells in IaC scripts as a first step towards developing approaches to improve IaC security. This first effort led to the unveiling of seven sins, limited by the focus on a single IaC tool as well as by the extensive, and potentially biased, manual effort that was required. We propose, in our work, to revisit this taxonomy: first, we extend the study of IaC security smells to a more diverse dataset with scripts associated with seven popular IaC tools, including Terraform, Ansible, Chef, Puppet, Pulumi, Saltstack, and Vagrant; second, we bring in some automation for the analysis by relying on an LLM. While we leverage LLMs for initial pattern processing, all taxonomic decisions underwent systematic human validation and reconciliation with established security standards. Our study yields a comprehensive taxonomy of 62 security smell categories, significantly expanding beyond the previously known seven. We demonstrate actionability by implementing new security checking rules within linters for seven popular IaC tools, often achieving 1.00 precision score. Our evolution study of security smells in GitHub projects reveals that these issues persist for extended periods, likely due to inadequate detection and mitigation tools. This work provides IaC practitioners with insights for addressing common security smells and systematically adopting DevSecOps practices to build safer infrastructure code.

## 📝 요약

이 논문은 인프라 코드(IaC) 스크립트의 보안 결함을 해결하기 위한 새로운 접근법을 제시합니다. 기존 연구는 단일 IaC 도구에 초점을 맞춰 보안 냄새의 분류를 제안했지만, 본 연구는 Terraform, Ansible 등 7개의 인기 있는 IaC 도구를 포함한 다양한 데이터셋을 분석합니다. LLM을 활용하여 자동화된 패턴 분석을 수행하고, 인간 검증을 통해 62개의 보안 냄새 카테고리를 제시합니다. 또한, 새로운 보안 검사 규칙을 구현하여 높은 정확도를 달성했습니다. GitHub 프로젝트 분석 결과, 보안 문제는 장기간 지속되며, 이는 탐지 및 완화 도구의 부족 때문임을 확인했습니다. 이 연구는 IaC 보안 개선과 DevSecOps 실천을 위한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 현대 소프트웨어 관리에 필수적인 코드형 인프라(IaC) 스크립트의 보안 결함은 심각한 결과를 초래할 수 있습니다.
- 2. 기존 연구는 IaC 스크립트의 보안 냄새에 대한 정확한 분류 체계 구축의 필요성을 인식했습니다.
- 3. 본 연구는 Terraform, Ansible, Chef 등 7개의 인기 있는 IaC 도구와 관련된 스크립트를 포함하여 보안 냄새 연구를 확장했습니다.
- 4. LLM을 활용하여 초기 패턴 처리를 자동화하고, 62개의 보안 냄새 카테고리를 포함하는 포괄적인 분류 체계를 제시했습니다.
- 5. GitHub 프로젝트의 보안 냄새 진화 연구는 이러한 문제가 장기간 지속됨을 보여주며, 이는 불충분한 탐지 및 완화 도구 때문입니다.


---

*Generated on 2025-09-24 14:02:08*