import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '07220000000',
  message: 'That is my number. please save it',
};

const quename = 'push_notification_code';

const job = queue.create(quename, jobData).save();

job.on('enqueue', () => console.log(`Notification job created: ${job.id}`))
  .on('complete', () => console.log('Notification job completed'))
  .on('error', () => console.error('Notification job failed'));
