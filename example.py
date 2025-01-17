from typing import Any, Dict, List, Tuple, Union


class MidPart:
    def __eq__(self, o: object) -> bool:
        if not isinstance(o, type(self)):
            raise TypeError(
                (
                    f"Cannot compare instance of {type(self).__name__} "
                    f"to instance of {type(o).__name__}"
                )
            )
        return self.__dict__ == o.__dict__

    def __repr__(self) -> str:
        return f"{type(self).__name__}({','.join([':'.join([repr(list(self.__init__.__annotations__.keys())[i]), repr(self.__dict__[x])]) for i, x in enumerate(self.__dict__)])})"

    def _generate_diffs_dictionary(self, o: object) -> Union[None, Dict[str, str]]:  # noqa
        diffs = {"section_name": type(self).__name__, "section_diffs": {}}

        if self != o:
            for key in self.__dict__:
                this_value = getattr(self, key)
                other_value = getattr(o, key)
                if this_value.strip().lower() != other_value.strip().lower():
                    diffs["section_diffs"][key] = [this_value, other_value]
            return diffs
        return None


class Profile(MidPart):
    def __init__(
        self, company_annual_turnover: str, country_of_primary_business_ops: str
    ) -> None:
        self.company_annual_turnover = company_annual_turnover
        self.country_of_primary_business_operations = country_of_primary_business_ops


class LegalAddress(MidPart):
    def __init__(
        self,
        line1: str,
        line2: str,
        line3: str,
        city: str,
        county: str,
        country: str,
        post_code: str,
    ) -> None:
        self.address_line_1 = line1
        self.address_line_2 = line2
        self.address_line_3 = line3
        self.city = city
        self.county = county
        self.country = country
        self.postal_code = post_code


class BusinessInfo(MidPart):
    def __init__(
        self, full_legal_name: str, biz_reg_num: str, country_of_formation: str
    ) -> None:
        self.full_legal_name = full_legal_name
        self.business_registration_number = biz_reg_num
        self.country_of_formation = country_of_formation


class AMLReview(MidPart):
    def __init__(
        self,
        SCDD: str,
        cst_doc_1_type: str,
        cst_doc_1_iss_agency: str,
        cst_doc_1_country: str,
    ) -> None:
        self.SCDD = SCDD
        self.cst_doc_1_document_type = cst_doc_1_type
        self.cst_doc_1_issuing_agency = cst_doc_1_iss_agency
        self.cst_doc_1_country = cst_doc_1_country


# class that will be inherited from PrincipalProofodIdentity
# and OwnershipAndControlDocs to avoid duplication
# as the fields are the same
class Document(MidPart):
    def __init__(
        self,
        doc_type: str,
        doc_num: str,
        issuing_agency: str,
        country: str,
        issue_date: str,
        expiry_date: str,
    ) -> None:
        self.document_type = doc_type
        self.document_number = doc_num
        self.issuing_agency = issuing_agency
        self.country = country
        self.issue_date = issue_date
        self.expiry_date = expiry_date

    def __getitem__(self, name: str) -> str:
        return self.__dict__[name]


class PrincipalProofOfIdentity(Document):
    def __init__(
        self,
        doc_type: str,
        doc_num: str,
        issuing_agency: str,
        country: str,
        issue_date: str,
        expiry_date: str,
    ) -> None:
        super().__init__(
            doc_type, doc_num, issuing_agency, country, issue_date, expiry_date
        )


class OwnershipAndControlDocument(Document):
    def __init__(
        self,
        doc_type: str,
        doc_num: str,
        issuing_agency: str,
        country: str,
        issue_date: str,
        expiry_date: str,
    ) -> None:
        super().__init__(
            doc_type, doc_num, issuing_agency, country, issue_date, expiry_date
        )


class AdditionalEvidenceOfIdentity(MidPart):
    def __init__(self, doc_type: str, description: str) -> None:
        self.document_type = doc_type
        self.description = description

    def __getitem__(self, name: str) -> str:
        return self.__dict__[name]


class PrincipalEntity(MidPart):
    def __init__(
        self,
        first_name: str,
        middle_name: str,
        last_name: str,
        principal_interest: str,
        beneficial_owner: str,
        responsible_party: str,
        authorized_signer: str,
        director: str,
        us_citizen: str,
        salutation: str,
        date_of_birth: str,
        address_line_1: str,
        address_line_2: str,
        city: str,
        postal_code: str,
        country: str,
        state_or_province: str,
        email: str,
        phone_int_code: str,
        mobile: str,
        phone: str,
        fax: str,
        citizenship1: str,
        citizenship2: str,
        cntr_of_perm_residence: str,
        proof_of_identity: PrincipalProofOfIdentity,
        add_evidence_of_identity: AdditionalEvidenceOfIdentity,
        ownership_docs: OwnershipAndControlDocument,
    ) -> None:
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.principal_interest = principal_interest
        self.beneficial_owner = beneficial_owner
        self.responsible_party = responsible_party
        self.authorized_signer = authorized_signer
        self.director = director
        self.us_citizen = us_citizen
        self.salutation = salutation
        self.date_of_birth = date_of_birth
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.postal_code = postal_code
        self.country = country
        self.state_or_province = state_or_province
        self.email = email
        self.phone_int_code = phone_int_code
        self.mobile = mobile
        self.phone = phone
        self.fax = fax
        self.citizenship1 = citizenship1
        self.citizenship2 = citizenship2
        self.country_of_permanent_residence = cntr_of_perm_residence
        self.proof_of_identity = proof_of_identity
        self.additional_evidence_of_identity = add_evidence_of_identity
        self.ownership_docs = ownership_docs

        self._id = (
            self.first_name.lower().strip() + "_" + self.last_name.lower().strip()
        )

    def __getitem__(self, name: str) -> str:
        return self.__dict__[name]


class IntermediateEntity(MidPart):
    def __init__(
        self,
        entity_name: str,
        address_line_1: str,
        address_line_2: str,
        city: str,
        postal_code: str,
        country: str,
        state: str,
        ownership: str,
    ) -> None:
        self.entity_name = entity_name
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.postal_code = postal_code
        self.country = country
        self.state = state
        self.ownership = ownership

    def __getitem__(self, name: str) -> str:
        return self.__dict__[name]


class EntityContainer(MidPart):
    def __init__(self, elements: List[Any]) -> None:
        self._elements = elements

    def __len__(self) -> int:
        return len(self._elements)

    def __iter__(self) -> Any:
        for elem in self._elements:
            yield elem


class PrincipalEntities(EntityContainer):
    def __init__(self, principal_entities: List[PrincipalEntity]) -> None:
        self._elements: List[PrincipalEntities] = principal_entities


class IntermediateEntities(EntityContainer):
    def __init__(self, intermediate_entities: List[IntermediateEntity]) -> None:
        self._elements = intermediate_entities


class PrincipalInfo(MidPart):
    def __init__(
        self,
        is_complex_struct: str,
        principal_entities: PrincipalEntities,
        intermediate_entities: IntermediateEntities = [],
    ) -> None:
        self.is_this_ownership_a_complex_structure = is_complex_struct
        self.principal_entities = principal_entities
        self.intermediate_entities = intermediate_entities

    def _compare_intermediate_entities(
        self, o: object
    ) -> Dict[str, Union[str, bool, List[Union[Dict[str, Any], Tuple[str]]]]]:  # noqa
        diffs = {
            "sub_section": "IntermediateEntities",
            "shared_ents_differences": [],
            "kyc_only_entities": [],
            "adloc_only_entities": [],
            "is_kyc_empty": False,
            "is_adloc_empty": False,
        }

        kyc_ents: IntermediateEntities = self.intermediate_entities
        adloc_ents: IntermediateEntities = o.intermediate_entities

        if len(kyc_ents) == 0:
            diffs["is_kyc_empty"] = True

        if len(adloc_ents) == 0:
            diffs["is_adloc_empty"] = True

        if len(kyc_ents) == 0 and len(adloc_ents) == 0:
            empty = IntermediateEntity(
                "THE GRID IS EMPTY - NO DATA", "", "", "", "", "", "", ""
            )
            empty_t = tuple([empty[field] for field in empty.__dict__])
            diffs["kyc_only_entities"].append(empty_t)
            diffs["adloc_only_entities"].append(empty_t)
            return diffs

        kyc_ent_names = [x["entity_name"] for x in kyc_ents]
        adloc_ent_names = [x["entity_name"] for x in adloc_ents]

        for name in kyc_ent_names:
            kyc_entity = [x for x in kyc_ents if x["entity_name"] == name][0]
            entity_fields = kyc_entity.__dict__

            if name not in adloc_ent_names:
                ent_tuple = tuple([kyc_entity[field] for field in entity_fields])

                diffs["kyc_only_entities"].append(ent_tuple)

            else:
                d = {"entity_name": kyc_entity["entity_name"], "field_diffs": {}}

                adloc_entity = [x for x in adloc_ents if x["entity_name"] == name][0]

                for field in entity_fields:
                    kyc_value = kyc_entity[field]
                    adl_value = adloc_entity[field]

                    try:
                        kyc_value_clean = (
                            kyc_value.strip().lower() if kyc_value else kyc_value
                        )
                    except AttributeError:
                        kyc_value_clean = kyc_value

                    try:
                        adl_value_clean = (
                            adl_value.strip().lower() if adl_value else adl_value
                        )
                    except AttributeError:
                        adl_value_clean = adl_value

                    if kyc_value_clean != adl_value_clean:
                        d["field_diffs"][field] = [kyc_value, adl_value]

                if len(d["field_diffs"].keys()) > 0:
                    diffs["shared_ents_differences"].append(d)

        for name in adloc_ent_names:
            adloc_entity = [x for x in adloc_ents if x["entity_name"] == name][0]

            entity_fields = adloc_entity.__dict__

            if name not in kyc_ent_names:
                ent_tuple = tuple([adloc_entity[field] for field in entity_fields])

                diffs["adloc_only_entities"].append(ent_tuple)

        if len(diffs["shared_ents_differences"]) == 0:
            if (
                len(diffs["kyc_only_entities"]) == 0
                and len(diffs["adloc_only_entities"]) == 0
            ):
                return None
            diffs.pop("shared_ents_differences")

        return diffs

    def _compare_principal_entities(
        self, o: object
    ) -> Dict[str, Union[str, List[Union[Dict[str, Any], Tuple[str]]]]]:  # noqa
        kyc_ents: PrincipalEntities = self.principal_entities
        adloc_ents: PrincipalEntities = o.principal_entities

        kyc_ent_names = [x["_id"] for x in kyc_ents]
        adloc_ent_names = [x["_id"] for x in adloc_ents]

        diffs = {
            "sub_section": "PrincipalEntities",
            "shared_ents_differences": [],
            "kyc_only_entities": [],
            "adloc_only_entities": [],
        }

        for name in kyc_ent_names:
            kyc_entity: PrincipalEntity = [x for x in kyc_ents if x["_id"] == name][0]
            entity_fields = kyc_entity.__dict__

            if name not in adloc_ent_names:
                vals = []
                for field in entity_fields:
                    if field != "_id":
                        if field in [
                            "proof_of_identity",
                            "additional_evidence_of_identity",
                            "ownership_docs",
                        ]:
                            t = tuple(
                                [
                                    kyc_entity[field][f]
                                    for f in kyc_entity[field].__dict__
                                ]
                            )
                        else:
                            t = kyc_entity[field]

                        vals.append(t)

                ent_tuple = tuple(vals)
                del vals
                diffs["kyc_only_entities"].append(ent_tuple)

            else:
                d = {
                    "entity_name": kyc_entity["first_name"]
                    + " "
                    + kyc_entity["last_name"],
                    "field_diffs": {},
                }

                adloc_entity = [x for x in adloc_ents if x["_id"] == name][0]

                for field in entity_fields:
                    if field != "_id":
                        if kyc_entity[field] != adloc_entity[field]:
                            if field in [
                                "proof_of_identity",
                                "additional_evidence_of_identity",
                                "ownership_docs",
                            ]:
                                kyc_t = tuple(
                                    [
                                        kyc_entity[field][f]
                                        for f in kyc_entity[field].__dict__
                                    ]
                                )

                                adl_t = tuple(
                                    [
                                        adloc_entity[field][f]
                                        for f in adloc_entity[field].__dict__
                                    ]
                                )

                                d["field_diffs"][field] = [kyc_t, adl_t]
                            else:
                                d["field_diffs"][field] = [
                                    kyc_entity[field],
                                    adloc_entity[field],
                                ]

                if len(d["field_diffs"].keys()) > 0:
                    diffs["shared_ents_differences"].append(d)

        for name in adloc_ent_names:
            adloc_entity: PrincipalEntity = [x for x in adloc_ents if x["_id"] == name][
                0
            ]

            entity_fields = adloc_entity.__dict__

            if name not in kyc_ent_names:
                vals = []
                for field in entity_fields:
                    if field != "_id":
                        if field in [
                            "proof_of_identity",
                            "additional_evidence_of_identity",
                            "ownership_docs",
                        ]:
                            t = tuple(
                                [
                                    adloc_entity[field][f]
                                    for f in adloc_entity[field].__dict__
                                ]
                            )

                        else:
                            t = adloc_entity[field]

                        vals.append(t)

                ent_tuple = tuple(vals)
                del vals
                diffs["adloc_only_entities"].append(ent_tuple)

        if len(diffs["shared_ents_differences"]) == 0:
            if (
                len(diffs["kyc_only_entities"]) == 0
                and len(diffs["adloc_only_entities"]) == 0
            ):
                return None
            diffs.pop("shared_ents_differences")

        return diffs

    def _generate_diffs_dictionary(self, o: object) -> Union[None, Dict[str, str]]:  # noqa
        diffs = {"section_name": "PrincipalInfo", "section_diffs": []}

        intermediate_entities_diffs = self._compare_intermediate_entities(o)
        principal_entities_diffs = self._compare_principal_entities(o)
        is_complex_structure_diff = (
            self.is_this_ownership_a_complex_structure
            != o.is_this_ownership_a_complex_structure
        )

        if is_complex_structure_diff:
            d = {
                "sub_section": "Is Complex Structure",
                "vals": [
                    self.is_this_ownership_a_complex_structure,
                    o.is_this_ownership_a_complex_structure,
                ],
            }
            diffs["section_diffs"].append(d)

        if intermediate_entities_diffs:
            diffs["section_diffs"].append(intermediate_entities_diffs)
        if principal_entities_diffs:
            diffs["section_diffs"].append(principal_entities_diffs)

        if len(diffs["section_diffs"]) == 0:
            return None

        return diffs


class Mid(MidPart):
    def __init__(
        self,
        mid_number: str,
        profile: Profile,
        legal_address: LegalAddress,
        business_info: BusinessInfo,
        aml_review: AMLReview,
        principal_info: PrincipalInfo,
    ) -> None:
        self.mid_number = mid_number
        self.profile = profile
        self.legal_address = legal_address
        self.business_info = business_info
        self.aml_review = aml_review
        self.principal_info = principal_info

        self.__post_init__()

    def __post_init__(self) -> None:
        self.__check_types()

    def __getitem__(self, name: str) -> str:
        return self.__dict__[name]

    def __check_types(self):
        annotations: Dict[str, Any] = self.__init__.__annotations__.copy()
        annotations.pop("return")

        for arg_name in annotations:
            expected_type: str = annotations[arg_name]
            actual_type: str = type(self.__dict__[arg_name])
            if actual_type != expected_type:
                raise TypeError(
                    f'"Mid" Class: Argument "{arg_name}" '
                    f'should be of type "{expected_type}", '
                    f'found type "{actual_type}"'
                )

    def get_diffs_from_other(self, o: object) -> Dict[str, str]:
        if type(o) is not type(self):
            raise TypeError(
                f"You cannot compare {type(self).__name__} to {type(o).__name__}"
            )

        diffs = {}
        diffs["kyc_mid"] = self.mid_number
        diffs["adloc_mid"] = o.mid_number
        diffs["diff_list"] = []

        comparison_keys = list(self.__dict__.keys())
        comparison_keys.remove("mid_number")

        for key in comparison_keys:
            this_section = self.__dict__[key]
            other_section = o.__dict__[key]
            sec_diffs = this_section._generate_diffs_dictionary(other_section)
            if sec_diffs:
                diffs["diff_list"].append(sec_diffs)
        return diffs
