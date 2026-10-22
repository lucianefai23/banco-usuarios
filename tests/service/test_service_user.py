import unittest
from src.service.service_user import ServiceUser

class TestServiceUser(unittest.TestCase):
    def test_add_user_success(self):
        name_add = 'Leonardo'
        job_add = 'TechLead'
        result_expect = 'Usuário adicionado com sucesso'
        service = ServiceUser()

        result = service.add_user(name=name_add, job=job_add)

        self.assertEqual(result_expect, result)

    def test_validate_null_job(self):
        name_null = 'Matheus'
        job_null = None
        result_expect = 'Os campos Nome ou Job não podem ser nulos'
        service = ServiceUser()

        result = service.add_user(name=name_null, job=job_null)

        self.assertEqual(result_expect, result)

    def test_validate_null_user(self):
        name_null = None
        job_null = 'Tester'
        resultado_esperado = 'Os campos Nome ou Job não podem ser nulos'
        service = ServiceUser()

        resultado = service.add_user(name=name_null, job=job_null)

        assert resultado_esperado == resultado

    def test_update_job_with_success(self):
        name = 'Thiago'
        job = 'TechLead'
        resultado_esperado = 'Profissão atualizada com sucesso'
        service = ServiceUser()

        resultado = service.update_user(name=name, new_job=job)

        assert resultado_esperado == resultado
