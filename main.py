import streamlit as st
from paho.mqtt import client as mqtt


def on_connect(client, userdata, flags, rc):
    st.success("Subscribed to " + subscribeTopic)
def on_disconnect(client, userdata, flags, rc):
    st.write("Disconnected")
def get_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish
    return client
def on_publish(client, userdata, mid):
    print("mid: " + str(mid))
def on_message(client, userdata, msg):
    st.write(msg.topic + " :: " + str(msg.payload))

st.title("MQTT CLIENT")
st.subheader("Web For Testing MQTT Connection")
col1, col2, col3 = st.columns(3)

with col1:
    broker = st.text_input("MQTT Broker", "mqtt.ardumeka.com")
    port = st.text_input("MQTT Port", "11219")
    client_id = st.text_input("Client ID", "ArduMeka91821")
    if st.button('Save Broker'):
        st.write(get_mqtt_client())

with col2:
    publishTopic = st.text_input("Publish Topic")
    message = st.text_input("Message")
    if st.button('Publish'):
        client = get_mqtt_client()
        client.on_publish = on_publish
        client.connect(broker, int(port), 60)
        client.publish(publishTopic, message)

with col3:
    subscribeTopic = st.text_input("Subscribe Topic")
    if st.button('Subscribe'):
        client = get_mqtt_client()
        client.on_message = on_message
        client.connect(broker, int(port), 60)
        client.subscribe(subscribeTopic)
        client.loop_forever()
        st.write("Subscribed to " + subscribeTopic)
