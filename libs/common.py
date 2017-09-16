import sys 

message_keys = {'server_key' : """*F)J@NcRfUjXn2r5u8x/A?D(G+KaPdSg""",
		'client_key' : """z$C&E)H@McQfTjWnZr4u7x!A$D*G-JaN""",
		  'user_key' : """6v9y$B&E(H+MbQeThWmZq4t7w!z*C*F-""",
	 	 'login_key' : """p2s5v8y/B?E(G+KbPeShVmYq3t6w9z$C""",
	  'login_successful' : """UjXn2r5u8x/A?D(G-KaPdSgVkYp3s6v9""",
	'login_unsuccessful' : """cQfTjWnZr4u7x!A@D*F-JaNdRgUkXp2s""",
		 'discovery' : """H+MbQeThWmZq4t7w!z_C*F)J@NcRfUjX""",
     'hardware_registration' : """?D(G+KbPeShVmYq3t6w9z$C&F)H@McQf""",
       'client_verification' : """x/A?D*G-KaPdSgVkYp3s6v9y$B&E)H+M""",
	'client_description' : """4u7x!A^C*F-JaNdRgUkXp2s5v8y/B?E(""",
		  'priority' : """mZq4t7w!z_C&F)J@NcRfUjXn2r5u8x/A""",
	       'sensor_edit' : """ShVmYq3t6w9z$C&E)H@McQfTjWnZr4u7""",
		'sensor_add' : """aPdSgVkYp3s6v9y$B&E(H+MbQeThWmZq""",
	      'ready_to_use' : """F-JaNdRgUkXp2s5v8y/B?E(G+KbPeShV""",
	   'acknowledgement' : """$C&F)J@NcRfUjXn2r5u8x/A?D*G-KaPd"""}

server_message_ports = {'broadcast_listener' : 65000,
			'broadcast_response' : 64001,
			   'login_listening' : 65333,
			    'login_response' : 64333,
				'tcp_server' : 65454}

client_message_ports = {'broadcast_port' : 64000,
           'broadcast_response_listener' : 65001,
                            'login_port' : 64333,
               'login_response_listener' : 65333}

login_unsuccessful_reason = {'server_error' : 0,
		  'username_not_recognized' : 1,
		       'password_incorrect' : 2,
			'already_logged_in' : 3}

create_account_unsuccessful = {'server_error' : 0,
                         'duplicate_username' : 1}

print(create_account_unsuccessful['server_error'])
