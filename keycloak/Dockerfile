FROM quay.io/keycloak/keycloak:latest as builder

ARG KC_HEALTH_ENABLED=true
ARG KC_METRICS_ENABLED=true
ARG KC_CACHE=ispn
ARG KC_CACHE_STACK=ispn
ARG KC_DB=mysql
ARG KC_TRANSACTION_XA_ENABLED=true
ARG KC_HTTP_RELATIVE_PATH="/"

ENV KC_HEALTH_ENABLED=${KC_HEALTH_ENABLED}
ENV KC_METRICS_ENABLED=${KC_METRICS_ENABLED}
ENV KC_CACHE=${KC_CACHE}
ENV KC_CACHE_STACK=${KC_CACHE_STACK}
ENV KC_DB=${KC_DB}
ENV KC_TRANSACTION_XA_ENABLED=${KC_TRANSACTION_XA_ENABLED}
ENV KC_HTTP_RELATIVE_PATH=${KC_HTTP_RELATIVE_PATH}

WORKDIR /opt/keycloak
RUN keytool -genkeypair -storepass password -storetype PKCS12 -keyalg RSA -keysize 2048 -dname "CN=server" -alias server -ext "SAN:c=DNS:localhost,IP:127.0.0.1" -keystore conf/server.keystore
RUN /opt/keycloak/bin/kc.sh build

FROM quay.io/keycloak/keycloak:latest
COPY --from=builder /opt/keycloak /opt/keycloak/

ENTRYPOINT ["/opt/keycloak/bin/kc.sh"]