package org.gem.log;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;

import org.junit.Ignore;

@Ignore
public class DummyAppender extends AMQPAppender {
    @Override
    protected Channel getChannel() {
        if (channel == null)
            channel = new DummyChannel();

        return channel;
    }

    @Override
    protected Connection getConnection() {
        return null;
    }
}
