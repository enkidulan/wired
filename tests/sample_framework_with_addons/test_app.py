def test_greet_a_customer(capsys):
    from an_app import main

    main()

    captured = capsys.readouterr()
    assert captured.out == "Hello !!\n"
