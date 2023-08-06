Introduction into RFB/VNC
*************************

.. important::
    Please note, that this section is not completed yet.

Messages
========

Security Types
--------------

.. todo

The protocol
============

Handshaking Phase
-----------------

.. mermaid::
    :align: center

    sequenceDiagram
        Server->>Client: max. possible ProtocolVersion
        Client-->>Server: answer with selected ProtocolVersion

        Server->>Client: send available SecurityTypes
        Client-->>Server: answer with selected SecurityType

        Note over Server,Client: Communication depending on selected security type

        Server->>Client: send SecurityResult

**Protocol for SecurityType 1 (NO-AUTHENTICATION):**

.. mermaid::
    :align: center

    sequenceDiagram
        Server->>Client: max. possible ProtocolVersion
        Client-->>Server: answer with selected ProtocolVersion

        Server->>Client: send available SecurityTypes
        Client-->>Server: answer with selected SecurityType

        Server->>Client: send SecurityResult

**Special Case for SecurityType 1 (NO-AUTHENTICATION) and ProtocolVersion 3.3/3.7:**

If the server and client decide to use the ProtocolVersion 3.3 or 3.7 and security type 1, the server does not send the
SecurityResult message, but will directly continue with the Initialization messages. This is valid for ProtocolVersion
3.3 [#rfc6143-v3.3-diffs]_ and 3.7 [#rfc6143-v3.7-diffs]_:

.. mermaid::
    :align: center

    sequenceDiagram
        Server->>Client: max. possible ProtocolVersion
        Client-->>Server: answer with selected ProtocolVersion

        Server->>Client: send selected SecurityType

        Note over Server,Client: Continue with Initialization messages

**Protocol for SecurityType 2 (VNC-AUTHENTICATION):**

.. mermaid::
    :align: center

    sequenceDiagram
        Server->>Client: max. possible ProtocolVersion
        Client-->>Server: answer with selected ProtocolVersion

        Server->>Client: send available SecurityTypes
        Client-->>Server: answer with selected SecurityType

        rect rgb(191, 223, 255)
        Server->>Client: send random 16-byte challenge
        Client-->>Server: DES encrypted challenge (with password)
        end

        Server->>Client: send SecurityResult

**Special Case for ProtocolVersion 3.3:**

If the server and client decide to use the ProtocolVersion 3.3, the handshaking phase changes. [#rfc6143-v3.3-diffs]_
Instead the server is provide a set of possible security types, it will just send a single security type. The
security-type may only take the value 0, 1, or 2.

.. mermaid::
    :align: center

    sequenceDiagram
        Server->>Client: max. possible ProtocolVersion
        Client-->>Server: answer with selected ProtocolVersion

        Server->>Client: send selected SecurityType

        Note over Server,Client: Communication depending on selected security type


Initialization Phase
--------------------

.. mermaid::
    :align: center

    sequenceDiagram

        Note over Server,Client: Handshaking Phase

        Client->>Server: ClientInit
        Server-->>Client: ServerInit

.. [#rfc6143-auth] https://datatracker.ietf.org/doc/html/rfc6143#section-7.2
.. [#rfc6143-auth-none] https://datatracker.ietf.org/doc/html/rfc6143#section-7.2.1
.. [#rfb6143-auth-vnc] https://datatracker.ietf.org/doc/html/rfc6143#section-7.2.2
.. [#rfc6143-v3.3-diffs] https://datatracker.ietf.org/doc/html/rfc6143#appendix-A.1
.. [#rfc6143-v3.7-diffs] https://datatracker.ietf.org/doc/html/rfc6143#appendix-A.2