#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer"""
    def test_no_arg(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([]), None)

    def test_identical(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([80, 80]), 80)

    def test_max_start(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([8, 6, 3]), 8)
    
    def test_normal_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 5, 0]), 5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([-1.5, -2.5, -3.5]), -1.5)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1.5, -2.5, 3.5]), 3.5)

    def test_ints_and_floats(self):
        self.assertEqual(max_integer([50, 50.8, -500, -0.5, 5000, 7000, -500000]), 7000)

    def test_one(self):
        self.assertEqual(max_integer([200]), 200)

    def test_numeric_string(self):
        self.assertEqual(max_integer("82625417398473"), "9")

    def test_positives_and_negatives_large(self):
        self.assertEqual(max_integer(
            [-6351, 9735, -8649, 4405, 6261, -1907, -9443, -6308,
                7474, -2513, 5721, 2319, 74, 7946, -5544, 7693, -7013,
                -6683, 715, -8738, 9678, -1081, 4730, -1376, 9126,
                7054, 545, 3492, -7285, -1672, 2230, -4576, -4121,
                9876, -537, 9823, 4281, -8003, 327, 1924, -1973, -9844,
                29, 3596, 1108, 6702, 4893, -9452, -5949, -9640, -2156,
                -4104, 5772, 5121, -2186, -4770, -4116, 6443, -9381,
                -9388, 8552, 3582, 3500, 7924, 211, -1176, 6346, -5405,
                899, -3432, -2550, -3353, 6944, 9623]), 9876)

    def test_ints_and_floats(self):
        self.assertEqual(max_integer([50, 50.8, -500, -0.5, 5000, 7000, -500000, 9999999999999999999, -9999999999999999999, 0.0001, -0.0001]), 9999999999999999999)

    def test_negatives(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
        max_integer(
            [-6105618, -854849, -562552, -3088955, -6711290, -4817844,
                -1907189, -8110534, -6601769, -5837524, -4726702,
                -8433749, -7251403, -5117635, -2979207, -1335257,
                -6867266, -9073637, -6224732, -1080801, -1080228,
                -6801278, -8351954, -1736432, -746131, -4376995,
                -967891, -4663691, -71560, -7153670, -8038202,
                -7893047, -9350883, -1132134, -3675971, -8495354,
                -9158229, -9310087, -6319598, -8961209, -4906000,
                -386471, -639929, -2676965, -6881679, -6258057,
                -5490677, -1107298, -4199148, -5933601, -9917695,
                -7759849, -7045734, -4885806, -9485075, -5119579,
                -4147063, -7622811, -4671971, -5439539, -840414,
                -3671742, -4400074, -3549343, -9146070, -6071672,
                -7213213, -1307446, -3936098, -2415520, -9162654,
                -6129976, -5791439, -3481890, -7828832, -6954726,
                -5272933, -4952516, -6115545, -8333464, -7271456,
                -4097027, -4342575, -8400559, -8235052, -4373818,
                -8054214, -8565596, -639225, -2292452, -4269529,
                -7202853, -6891036, -4379807, -7955196, -1536591,
                -2839083, -2586661, -9941097, -3136620]), -71560)

    def test_ints_and_floats_large(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
        max_integer(
            [199872.761905, 115249.881356, 37972.944444, 120549.903226,
                30889.777778, 986136.4, 393382.541667, 15441.826087,
                2503568, 176118.871795, 372359.4, 142747.615385,
                383318.818182, 297732.272727, 104980.527027, 98409.272727,
                617459.875, 56556.621622, 61958.8, 115000.590909,
                240958.457143, 101071.857143, 77616.476923, 89029.64,
                104941.966667, 31940.538462, 106652.101266,
                686700.153846, 52758.709677, 348259.428571, 89457.289474,
                58039.527027, 306427.535714, 64379.011765, 557699.533333,
                18718.639344, 364967.555556, 129951.234043,
                41683.826923, 139149.981818, 356782.866667,
                100259.076923, 245204.75, 78972.530612, 404825.888889,
                124364.25, 1065047.5, 42946.45614, 73670.881356,
                83546.513514, 323098.333333, 88578.352941, 89471.0,
                47745.197917, 17102.676768, 127735.808824,
                110513.058824, 62214.055556, 6968.981481, 40691.346939,
                69931.096774, 67024.44186, 112123.04, 1167186.0,
                140392.05, 15814.362637, 88923.344444, 114726.207317,
                143303.55, 38233.835165, 94065.728571, 42789.892857,
                44182.471698, 41313.101266, 67705.189655, 1222423.5,
                44966.554054, 37153.6, 82085.08, 559793.285714,
                30031.588235, 126947.42623, 309222.3125, 125132.820896,
                37276.273973, 99726.629032, 4270.788235, 490468.4375,
                54086.642857, 73068.5, 108526.508197, 52943.875,
                128534.875, 61069.433333, 37142.719512, 51481.131148,
                571618.5, 35977.166667, 142333.117647, 199123.75]), 2503568)

    def test_floats(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
        max_integer(
            [0.00124, 0.457569, 0.02346, 0.23423435, 0.45675675, 0.678679,
                0.867091, 0.74654, 0.5745376]), 0.867091)

    def test_floats_large(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
        max_integer(
            [0.3670144948698114, 0.22932193120425425, 17.269673745943178,
                0.6021998063297005, 7.040663644666582, 0.3184181530984761,
                0.14782568486828356, 1.6941500966097131, 0.5232924790473241,
                6.5772783880035, 0.03165696316739836,
                0.9723205356754643, 1.0167973840532783,
                0.17994528432150623, 0.3426895920314973,
                0.8237893847200374, 6.564703466354199, 0.6509432044790271,
                1.8902940005294794, 7.691604865311828, 8.897302744173897,
                1.0780411284398353, 1.6564018996809177,
                0.7495378363397326, 0.6460418901123864,
                0.29656944388569285, 1.2020859950744734,
                2.695758513783995, 0.3729333928560498,
                0.8540047898304737, 0.16021193325291795,
                0.02789189111717051, 0.8464685760135893,
                4.506719557284898, 2.025804108780801, 4.525163681550945,
                1.3277284362225875, 3.042753010712082, 2.4201460936424987,
                0.6254206993310947, 3.6037820704785767,
                0.584394275327247, 2.99405593244928, 0.5168645505697169,
                0.014982685631661027, 0.02477737364433172,
                0.47120480947220956, 2.5056796257122916,
                1.3349487122618869, 0.08451917751917886,
                1.0157082402123357, 29.496355326217377,
                10.171800729369349, 1.1263544935158728,
                0.4757292903555028, 3.7123230733757541,
                0.5742929278531705, 0.43940976988732967,
                0.09537099783126888, 1.4936141049902175,
                5.764320019082693, 4.322880498170904, 2.004237813008688,
                0.55652435810246, 4.302022962278393, 5.680293004785563,
                2.178866303290744, 1.0390412554953966,
                0.4513255136189632, 1.4643609109467474,
                0.6904822043628015, 7.428505996709021, 0.8174242076055684,
                0.656098688607157, 0.651301664737984,
                0.7402037152516, 1.3480227709351068, 10.667222236398728,
                1.1255361340134916, 0.3631658619504304,
                0.8812949657884554, 1.1100323642668829,
                5.011964346018885, 2.8953551308720057,
                2.557432463236887, 9.16949364230712, 0.41756927084445695,
                2.3447489446054015, 1.167426159062932,
                0.6998588019912836, 0.427705761254529,
                1.7136005979522014, 8.877571036363526,
                0.6825287480571864, 2.683429465021834,
                0.7504024417975862, 0.2762206358275794,
                0.20607476376994403, 0.9497689034126078,
                2.1498649449691808]), 29.496355326217377)
    def test_string_input(self):
        """Unittest for max_integer with numeric string input"""
        self.assertEqual(max_integer("192834754"), "9")

    def test_char_input(self):
	    """Unittest for max_integer with character input"""
		    self.assertEqual(max_integer("Hollton"), "t")

    def test_list_of_lists(self):
	"""Unittest for max_integer with a list of lists"""
		self.assertEqual(max_integer([[], [2], [4], [2, 9]]), [4])

    def test_str_list_input(self):
	    """Unittest for max_integer with a list of strings"""
		    self.assertEqual(
				    max_integer([["foo"], ["boo"], ["abc"], ["yic"], ["aic"]]), ["yic"])

def test_infinity_input(self):
    """Unittest for max_integer with infinity in the input"""
    self.assertEqual(max_integer([99, float('inf'), float('-inf')]),
                     float('inf'))

def test_nan_input(self):
    """Unittest for max_integer with NaN in the input"""
    self.assertEqual(max_integer([999, float('nan'), 1000]), 1000)

    def test_mixed_list(self):
        """Unittest for max_integer([..])"""
		with self.assertRaises(TypeError):
			max_integer([[], [2], [4], [2, 9], 99, "foo"])

    def test_different_types_in_list(self):
	    """Check if max_integer handles a list with various data types."""
		    with self.assertRaises(TypeError):
			    max_integer([[], [2], [4], [2, 9], 99, "foo"])

     def test_integer_and_string_mixed_list(self):
	     """Verify max_integer behavior with a list containing both integers and strings."""
		     with self.assertRaises(TypeError):
			     max_integer([99, "foo"])

    def test_input_none(self):
	    """Validate max_integer response when given None."""
		    with self.assertRaises(TypeError):
			    max_integer(None)

    def test_dictionary_input(self):
	    """Test max_integer behavior with a list containing dictionaries."""
		    with self.assertRaises(TypeError):
			    max_integer([{20: 23, 14: 45}, {"a": "b"}])

    def test_integer_input(self):
	    """Check max_integer handling for a single integer."""
		    with self.assertRaises(TypeError):
			    max_integer(98)

    def test_float_input(self):
	    """Evaluate max_integer response with a single float."""
		    with self.assertRaises(TypeError):
			    max_integer(9.8)

if __name__ == '__main__':
    unittest.main()
